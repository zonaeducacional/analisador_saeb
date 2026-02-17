"""
Módulo para Parsing de Arquivos (PDF, DOCX, Imagens)
Extrai questões de múltipla escolha automaticamente
"""

import re
import io
from pathlib import Path
from typing import List, Dict, Tuple

try:
    import PyPDF2
except ImportError:
    PyPDF2 = None

try:
    from docx import Document
except ImportError:
    Document = None

try:
    from PIL import Image
except ImportError:
    Image = None

# easyocr será carregado sob demanda para evitar problemas em deploy
easyocr = None
READER = None


class ParserArquivos:
    """Parser para extrair questões de diferentes formatos de arquivo"""
    
    def __init__(self):
        self.leitor_ocr = None
    
    def _carregar_ocr(self):
        """Carrega modelo OCR sob demanda"""
        global READER, easyocr
        
        if READER is not None:
            return READER
        
        try:
            import easyocr as eocr
            easyocr = eocr
            READER = easyocr.Reader(['pt'], gpu=False)
            return READER
        except Exception as e:
            raise RuntimeError(f"Erro ao carregar OCR: {str(e)}")
    
    def processar_arquivo(self, arquivo_bytes, nome_arquivo: str) -> Tuple[List[Dict], str]:
        """
        Processa arquivo e extrai questões
        
        Args:
            arquivo_bytes: Conteúdo do arquivo em bytes
            nome_arquivo: Nome do arquivo
            
        Returns:
            Tupla (lista_questoes, mensagem_status)
        """
        extensao = Path(nome_arquivo).suffix.lower()
        
        if extensao == '.pdf':
            return self._processar_pdf(arquivo_bytes)
        elif extensao == '.docx':
            return self._processar_docx(arquivo_bytes)
        elif extensao in ['.png', '.jpg', '.jpeg', '.bmp', '.gif']:
            return self._processar_imagem(arquivo_bytes, extensao)
        else:
            return [], f"❌ Formato não suportado: {extensao}"
    
    def _processar_pdf(self, arquivo_bytes) -> Tuple[List[Dict], str]:
        """Extrai texto de PDF"""
        if PyPDF2 is None:
            return [], "❌ PyPDF2 não está instalado"
        
        try:
            pdf_file = io.BytesIO(arquivo_bytes)
            leitor = PyPDF2.PdfReader(pdf_file)
            texto = ""
            
            for pagina in leitor.pages:
                texto += pagina.extract_text() + "\n"
            
            questoes = self._extrair_questoes_do_texto(texto)
            
            if questoes:
                return questoes, f"✅ {len(questoes)} questão(ões) extraída(s) do PDF"
            else:
                return [], "⚠️ Nenhuma questão encontrada no PDF"
        
        except Exception as e:
            return [], f"❌ Erro ao processar PDF: {str(e)}"
    
    def _processar_docx(self, arquivo_bytes) -> Tuple[List[Dict], str]:
        """Extrai texto de DOCX"""
        if Document is None:
            return [], "❌ python-docx não está instalado"
        
        try:
            docx_file = io.BytesIO(arquivo_bytes)
            doc = Document(docx_file)
            texto = "\n".join([p.text for p in doc.paragraphs])
            
            questoes = self._extrair_questoes_do_texto(texto)
            
            if questoes:
                return questoes, f"✅ {len(questoes)} questão(ões) extraída(s) do DOCX"
            else:
                return [], "⚠️ Nenhuma questão encontrada no DOCX"
        
        except Exception as e:
            return [], f"❌ Erro ao processar DOCX: {str(e)}"
    
    def _processar_imagem(self, arquivo_bytes, extensao) -> Tuple[List[Dict], str]:
        """Usa OCR para extrair texto de imagem"""
        
        if Image is None:
            return [], "❌ Pillow não está instalado"
        
        try:
            import streamlit as st
            
            # Carregar modelo OCR sob demanda
            with st.spinner("🔄 Inicializando OCR (primeira vez pode demorar ~1-2 min)..."):
                leitor_ocr = self._carregar_ocr()
            
            # Carregar imagem
            imagem = Image.open(io.BytesIO(arquivo_bytes))
            
            # Fazer OCR
            with st.spinner("🔄 Processando imagem com OCR..."):
                resultado = leitor_ocr.readtext(imagem, detail=0)
            
            texto = "\n".join(resultado)
            
            questoes = self._extrair_questoes_do_texto(texto)
            
            if questoes:
                return questoes, f"✅ {len(questoes)} questão(ões) extraída(s) da imagem via OCR"
            else:
                return [], "⚠️ Nenhuma questão encontrada na imagem"
        
        except Exception as e:
            return [], f"❌ Erro ao processar imagem: {str(e)}"
    
    def _extrair_questoes_do_texto(self, texto: str) -> List[Dict]:
        """
        Extrai questões de múltipla escolha do texto
        Procura por padrão: Questão X / Q X / Questão X:
        Seguindo por alternativas A), B), C), D)
        """
        questoes = []
        linhas = texto.split('\n')
        
        i = 0
        numero_questao = 1
        
        while i < len(linhas):
            linha = linhas[i].strip()
            
            # Procurar por início de questão
            if re.match(r'^(questão|q|q\.|questão)\s*[\d]+', linha, re.IGNORECASE):
                questao_dict = self._extrair_questao_bloco(linhas, i)
                
                if questao_dict.get('alternativas'):
                    questao_dict['id'] = numero_questao
                    questoes.append(questao_dict)
                    numero_questao += 1
                    i += questao_dict.get('linhas_processadas', 1)
                else:
                    i += 1
            else:
                i += 1
        
        return questoes
    
    def _extrair_questao_bloco(self, linhas: List[str], indice_inicio: int) -> Dict:
        """Extrai uma questão completa começando em um índice"""
        questao = {
            'enunciado': '',
            'alternativas': {},
            'linhas_processadas': 0
        }
        
        i = indice_inicio
        blocos_enunciado = []
        alternativas_encontradas = {}
        
        # Coletar enunciado
        while i < len(linhas):
            linha = linhas[i].strip()
            
            # Verificar se é uma alternativa
            if re.match(r'^[a-dA-D]\)', linha):
                # Encontrou primeira alternativa
                break
            
            if linha and not re.match(r'^(questão|q|q\.)', linha, re.IGNORECASE):
                blocos_enunciado.append(linha)
            
            i += 1
        
        questao['enunciado'] = ' '.join(blocos_enunciado)
        
        # Coletar alternativas
        while i < len(linhas):
            linha = linhas[i].strip()
            
            # Padrão: A) texto, B) texto, etc
            match = re.match(r'^([a-dA-D])\)\s*(.*)', linha)
            if match:
                letra = match.group(1).upper()
                texto = match.group(2)
                alternativas_encontradas[letra] = texto
                i += 1
            elif re.match(r'^[a-dA-D]\)', linha):
                i += 1
            elif linha and re.match(r'^(questão|q|q\.)', linha, re.IGNORECASE):
                # Encontrou próxima questão
                break
            elif not linha:
                # Linha vazia, continua
                i += 1
            else:
                # Pode ser continuação de alternativa anterior
                if alternativas_encontradas:
                    ultima_letra = list(alternativas_encontradas.keys())[-1]
                    alternativas_encontradas[ultima_letra] += ' ' + linha
                i += 1
        
        questao['alternativas'] = alternativas_encontradas
        questao['linhas_processadas'] = i - indice_inicio
        
        return questao if alternativas_encontradas else {}


def formatar_questoes_extraidas(questoes: List[Dict]) -> List[Dict]:
    """
    Formata questões extraídas para o formato esperado pelo analisador
    Sem resposta_correta nem descritor (O usuário fornecerá)
    """
    formatadas = []
    
    for q in questoes:
        formatada = {
            'id': q.get('id', len(formatadas) + 1),
            'enunciado': q.get('enunciado', ''),
            'alternativas': q.get('alternativas', {}),
            'descritor': None,  # Será definido pelo usuário
            'resposta_usuario': None,  # Será definida pelo usuário
            'tipo_texto': 'Extraído de arquivo'
        }
        formatadas.append(formatada)
    
    return formatadas
