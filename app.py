"""App principal - Corretor de Questões SAEB de Múltipla Escolha"""

import streamlit as st
import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent))

from src.analisador import AnalisadorQuestoes
from src.prompt_generator import GeradorPromptsQuestoes
from src.questoes_saeb import listar_todas_questoes, obter_descritores_unicos
from src.file_parser import ParserArquivos, formatar_questoes_extraidas

# Configuração da página
st.set_page_config(
    page_title="Corretor SAEB - Questões de Múltipla Escolha",
    page_icon="✏️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo customizado
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        color: white;
    }
    .info-box {
        background-color: #e3f2fd;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #2196f3;
        margin-bottom: 15px;
        color: #000 !important;
    }
    .info-box h3, .info-box p, .info-box strong {
        color: #000 !important;
    }
    .success-box {
        background-color: #e8f5e9;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #4caf50;
        margin-bottom: 15px;
        color: #000 !important;
    }
    .success-box h3, .success-box p, .success-box strong {
        color: #000 !important;
    }
    .error-box {
        background-color: #ffebee;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #f44336;
        margin-bottom: 15px;
        color: #000 !important;
    }
    .error-box h3, .error-box p, .error-box strong {
        color: #000 !important;
    }
    .resultado-box {
        background-color: #fff9c4;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #ff9800;
        margin-bottom: 15px;
        color: #000 !important;
    }
    .resultado-box h3, .resultado-box p, .resultado-box strong {
        color: #000 !important;
    }
</style>
""", unsafe_allow_html=True)

def init_session_state():
    """Inicializa variáveis de sessão"""
    if "analise_realizada" not in st.session_state:
        st.session_state.analise_realizada = False
    if "resultado_analise" not in st.session_state:
        st.session_state.resultado_analise = None
    if "questoes_respondidas" not in st.session_state:
        st.session_state.questoes_respondidas = {}
    if "questoes_extraidas" not in st.session_state:
        st.session_state.questoes_extraidas = None
    if "arquivo_processado" not in st.session_state:
        st.session_state.arquivo_processado = False
    if "analise_arquivo" not in st.session_state:
        st.session_state.analise_arquivo = None
    if "mensagem_extracao" not in st.session_state:
        st.session_state.mensagem_extracao = ""

def copiar_para_clipboard(texto, label="📋 Copiar para Clipboard"):
    """Cria um componente para copiar texto enviando como download primeiro"""
    col1, col2 = st.columns([1, 0.2])
    
    with col1:
        st.text_area(
            "Prompt:",
            value=texto,
            height=400,
            disabled=True,
            label_visibility="collapsed"
        )
    
    with col2:
        # Usando download como alternativa
        st.download_button(
            label=label,
            data=texto,
            file_name="prompt_saeb.txt",
            mime="text/plain",
            use_container_width=True
        )
        
        st.markdown("""
        <div style="text-align: center; margin-top: 10px; font-size: 12px; color: #666;">
        O arquivo será baixado.<br/>Cole o conteúdo onde quiser.
        </div>
        """, unsafe_allow_html=True)

def main():
    """Função principal"""
    init_session_state()
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>✏️ Corretor de Questões SAEB</h1>
        <p>Análise e Feedback para Questões de Múltipla Escolha</p>
        <p>Português 9º Ano</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configurações")
        
        modo = st.radio(
            "Escolha o modo:",
            ["📋 Analisar uma Questão", "📊 Analisar Múltiplas", "📤 Upload de Arquivo", "🔍 Consultar Questões", "ℹ️ Sobre Descritores"],
            help="Selecione como deseja usar o corretor"
        )
        
        st.divider()
        st.info("""
        ℹ️ **Como usar:**
        1. Selecione uma questão
        2. Escolha sua resposta (A, B, C ou D)
        3. Clique em "Analisar"
        4. Copie o prompt gerado
        5. Cole em ChatGPT ou outra IA
        """)
    
    # Conteúdo principal
    if modo == "📋 Analisar uma Questão":
        st.header("Análise Individual de Questão")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Selecione a Questão")
            questoes = listar_todas_questoes()
            opcoes_questoes = {f"Q{q['id']} - {q['descritor']}: {q['competencia'][:40]}...": q['id'] for q in questoes}
            
            questao_selecionada_texto = st.selectbox(
                "Questões disponíveis:",
                list(opcoes_questoes.keys()),
                label_visibility="collapsed"
            )
            
            id_questao = opcoes_questoes[questao_selecionada_texto]
            questao = next(q for q in questoes if q['id'] == id_questao)
            
            # Mostrar questão
            with st.expander("📖 Ver Enunciado", expanded=True):
                st.markdown(questao['enunciado'])
                
                st.write("**Alternativas:**")
                for alt, texto in questao['alternativas'].items():
                    st.write(f"**{alt})** {texto}")
        
        with col2:
            st.subheader("Sua Resposta")
            
            resposta = st.radio(
                "Escolha sua resposta:",
                ["A", "B", "C", "D"],
                label_visibility="collapsed",
                horizontal=True
            )
            
            st.write("")
            
            if st.button("🔍 Analisar Resposta", use_container_width=True, type="primary"):
                analisador = AnalisadorQuestoes()
                resultado = analisador.analisar_resposta(id_questao, resposta)
                st.session_state.resultado_analise = resultado
                st.session_state.analise_realizada = True
                st.rerun()
        
        # Mostrar resultado
        if st.session_state.analise_realizada and st.session_state.resultado_analise:
            st.divider()
            resultado = st.session_state.resultado_analise
            
            # Feedback imediato
            if resultado["acertou"]:
                st.markdown(f"""
                <div class="success-box">
                <h3>✅ Parabéns! Você acertou!</h3>
                <p><strong>Você escolheu:</strong> {resultado['resposta_aluno']} - "{questao['alternativas'][resultado['resposta_aluno']]}"</p>
                <p><strong>Descritor:</strong> {resultado['descritor']} - {resultado['competencia']}</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="error-box">
                <h3>❌ Sua resposta está incorreta</h3>
                <p><strong>Você escolheu:</strong> {resultado['resposta_aluno']} - "{questao['alternativas'][resultado['resposta_aluno']]}"</p>
                <p><strong>Resposta correta:</strong> {resultado['resposta_correta']} - "{questao['alternativas'][resultado['resposta_correta']]}"</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Explicação
            with st.expander("💡 Explicação", expanded=True):
                st.write(resultado['justificativa'])
                
                st.write("**Descritor Avaliado:**")
                st.write(f"{resultado['descritor']} - {resultado['competencia']}")
            
            # Sugestões
            with st.expander("📚 Como Responder Corretamente"):
                analisador = AnalisadorQuestoes()
                sugestoes = analisador.obter_sugestoes_melhoria(id_questao)
                
                st.write("**Passo a Passo para Resolver:**")
                for passo in sugestoes['passo_a_passo']:
                    st.write(passo)
            
            st.divider()
            
            # Gerar prompt
            st.subheader("🤖 Gerar Prompt para IA")
            st.info("Clique abaixo para gerar um prompt que pode ser usado em ChatGPT, Claude ou outra IA para obter feedback detalhado.")
            
            if st.button("📋 Gerar Prompt Completo", use_container_width=True):
                gerador = GeradorPromptsQuestoes()
                prompt = gerador.gerar_prompt_correcao_completa(resultado)
                
                st.markdown("### 📄 Prompt para IA")
                copiar_para_clipboard(prompt, "📥 Baixar Prompt")
    
    elif modo == "📊 Analisar Múltiplas":
        st.header("Análise de Múltiplas Questões")
        
        st.info("Responda várias questões para obter análise comparativa e identificar descritores mais fraco.")
        
        questoes = listar_todas_questoes()
        
        # Criar interface de resposta
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📝 Responda as Questões")
            
            for questao in questoes:
                with st.expander(f"Q{questao['id']} - {questao['descritor']}: {questao['competencia'][:35]}..."):
                    st.write(questao['enunciado'][:200] + "...")
                    
                    resposta = st.radio(
                        "Sua resposta:",
                        ["A", "B", "C", "D"],
                        key=f"q_{questao['id']}"
                    )
                    
                    st.session_state.questoes_respondidas[questao['id']] = resposta
        
        with col2:
            st.subheader("📊 Análise")
            
            if st.button("📊 Analisar Todas", use_container_width=True, type="primary"):
                if st.session_state.questoes_respondidas:
                    analisador = AnalisadorQuestoes()
                    analise = analisador.analisar_multiplas_respostas(st.session_state.questoes_respondidas)
                    st.session_state.resultado_analise = analise
                    st.session_state.analise_realizada = True
                    st.rerun()
        
        # Mostrar resultado agregado
        if st.session_state.analise_realizada and st.session_state.resultado_analise:
            st.divider()
            analise = st.session_state.resultado_analise
            
            # Cards de resumo
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Total", analise['total_questoes'])
            
            with col2:
                st.metric("Acertos", analise['acertos'])
            
            with col3:
                st.metric("Erros", analise['erros'])
            
            with col4:
                st.metric("Taxa %", f"{analise['percentual_acerto']:.1f}%")
            
            # Análise por descritor
            with st.expander("🎯 Análise por Descritor", expanded=True):
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("**✅ Descritores Forte:**")
                    if analise['descritores_fortes']:
                        for desc in analise['descritores_fortes']:
                            st.write(f"• {desc}")
                    else:
                        st.write("Nenhum")
                
                with col2:
                    st.write("**⚠️ Descritores Fraco:**")
                    if analise['descritores_fraco']:
                        for desc in analise['descritores_fraco']:
                            st.write(f"• {desc}")
                    else:
                        st.write("Nenhum")
            
            # Detalhes de cada questão
            with st.expander("📋 Detalhes das Questões"):
                for resultado in analise['resultados_individuais']:
                    status = "✅" if resultado['acertou'] else "❌"
                    st.write(f"{status} **Q{resultado['questao_id']} - {resultado['descritor']}**")
                    st.write(f"Você respondeu: {resultado['resposta_aluno']} | Correta: {resultado['resposta_correta']}")
            
            # Gerar prompt
            st.divider()
            st.subheader("🤖 Gerar Relatório para IA")
            
            if st.button("📄 Gerar Prompt de Relatório", use_container_width=True):
                gerador = GeradorPromptsQuestoes()
                prompt = gerador.gerar_prompt_multiplas_questoes(analise)
                
                copiar_para_clipboard(prompt, "📥 Baixar Relatório")
    
    elif modo == "📤 Upload de Arquivo":
        st.header("Analisar Questões do Arquivo")
        
        st.info("""
        📤 **Upload de Arquivo**
        - Suporte para PDF, DOCX e Imagens (JPG, PNG)
        - Sistema extrai questões automaticamente
        - Você confirma e responde as questões
        - Análise nos mesmos moldes do sistema
        """)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📁 Upload do Arquivo")
            arquivo = st.file_uploader(
                "Selecione um arquivo:",
                type=["pdf", "docx", "jpg", "jpeg", "png", "bmp"],
                label_visibility="collapsed"
            )
            
            if arquivo:
                st.markdown(f"**Arquivo selecionado:** {arquivo.name}")
                
                if st.button("🔍 Extrair Questões", use_container_width=True, type="primary"):
                    st.session_state.arquivo_processado = True
                    
                    with st.spinner("🔄 Processando arquivo..."):
                        parser = ParserArquivos()
                        questoes_extraidas, mensagem = parser.processar_arquivo(
                            arquivo.read(),
                            arquivo.name
                        )
                    
                    st.session_state.questoes_extraidas = formatar_questoes_extraidas(questoes_extraidas)
                    st.session_state.mensagem_extracao = mensagem
                    st.rerun()
        
        with col2:
            st.subheader("📋 Informações")
            st.write("""
            **Formatos suportados:**
            - 📄 PDF
            - 📝 DOCX
            - 🖼️ Imagens (JPG, PNG)
            
            **Como funciona:**
            1. Suba seu arquivo com as questões
            2. Sistema extrai automaticamente
            3. Confirme as questões extraídas
            4. Responda cada uma
            5. Receba análise completa
            """)
        
        # Mostrar resultado da extração
        if hasattr(st.session_state, 'questoes_extraidas') and st.session_state.questoes_extraidas:
            st.divider()
            
            # Mensagem de status
            st.markdown(f"<div class='resultado-box'>{st.session_state.mensagem_extracao}</div>", unsafe_allow_html=True)
            
            questoes_arquivo = st.session_state.questoes_extraidas
            
            st.subheader(f"📋 {len(questoes_arquivo)} Questão(ões) Extraída(s)")
            
            # Permitir responder as questões
            respostas = {}
            
            for i, q in enumerate(questoes_arquivo, 1):
                with st.expander(f"Questão {i}", expanded=(i==1)):
                    st.write(f"**Enunciado:**\n{q['enunciado']}")
                    
                    st.write("\n**Alternativas:**")
                    alternativas_lista = []
                    for letra in ['A', 'B', 'C', 'D']:
                        if letra in q['alternativas']:
                            texto = q['alternativas'][letra]
                            st.write(f"**{letra})** {texto}")
                            alternativas_lista.append(letra)
                    
                    # Input para resposta
                    resposta = st.radio(
                        "Sua resposta:",
                        alternativas_lista,
                        key=f"arquivo_resposta_{q['id']}"
                    )
                    
                    respostas[q['id']] = resposta
            
            st.divider()
            
            if st.button("📊 Analisar Todas as Questões", use_container_width=True, type="primary"):
                # Mapear IDs para índices do array para análise personalizada
                analisador = AnalisadorQuestoes()
                analise_resultados = []
                
                for idx, questao in enumerate(questoes_arquivo):
                    q_id = questao['id']
                    if q_id in respostas:
                        resultado = {
                            "questao_id": q_id,
                            "enunciado": questao['enunciado'],
                            "alternativas": questao['alternativas'],
                            "resposta_aluno": respostas[q_id],
                            "resposta_correta": "?",  # Não temos resposta correta
                            "acertou": False,  # Não sabemos sem resposta correta
                            "tipo_texto": questao.get('tipo_texto', 'Extraído de arquivo'),
                            "descritor": "Desconhecido",
                            "competencia": "Questão extraída de arquivo",
                            "justificativa": "Use IA para verificar a resposta correta",
                            "sugestoes_procedimentais": [],
                            "feedback": f"Você respondeu: {respostas[q_id]}. Consulte a IA para verficar se está correto.",
                            "pontuacao": 0
                        }
                        analise_resultados.append(resultado)
                
                st.session_state.analise_arquivo = analise_resultados
                st.rerun()
            
            # Mostrar análise se já foi feita
            if hasattr(st.session_state, 'analise_arquivo'):
                st.divider()
                st.subheader("📊 Análise das Questões")
                
                for resultado in st.session_state.analise_arquivo:
                    with st.expander(f"Questão {resultado['questao_id']}: Sua resposta foi {resultado['resposta_aluno']}"):
                        st.write(f"**Enunciado:**\n{resultado['enunciado']}")
                        st.write(f"\n**Sua resposta:** {resultado['resposta_aluno']}")
                        st.info(resultado['feedback'])
                
                # Gerar prompt para IA analisar
                st.divider()
                st.subheader("🤖 Gerar Relatório para IA")
                
                if st.button("📄 Gerar Análise Completa pela IA", use_container_width=True):
                    gerador = GeradorPromptsQuestoes()
                    
                    # Criar prompt com questões do arquivo
                    prompt = f"""# ANÁLISE DE QUESTÕES EXTRAÍDAS DE ARQUIVO

## Resumo das Questões
Total de questões: {len(st.session_state.analise_arquivo)}

## Questões e Respostas do Aluno

"""
                    
                    for res in st.session_state.analise_arquivo:
                        prompt += f"""
### Questão {res['questao_id']}
**Enunciado:** {res['enunciado']}

**Alternativas:**
"""
                        for letra, texto in res['alternativas'].items():
                            prompt += f"{letra}) {texto}\n"
                        
                        prompt += f"\n**Resposta do aluno:** {res['resposta_aluno']}\n"
                    
                    prompt += """

---

## INSTRUÇÕES PARA ANÁLISE

Você está analisando questões extraídas de um arquivo enviado por um educador.

### IMPORTANTE:
- Você NÃO conhece as respostas corretas
- Mas pode analisar a qualidade das questões e a lógica das respostas
- Forneça feedback construtivo sobre cada resposta

### PARA CADA QUESTÃO:
1. Analise o enunciado e as alternativas
2. Comente sobre a resposta escolhida pelo aluno
3. Sugira possíveis erros comuns
4. Indique se a resposta parece lógica
5. Proponha caminhos para verificar a resposta correta

### ESTRUTURA DO RELATÓRIO:
- Análise individual de cada questão
- Padrões observados nas respostas
- Sugestões gerais de estudo

Gere agora uma análise educativa, construtiva e motivadora.
"""
                    
                    copiar_para_clipboard(prompt, "📥 Baixar Análise")
    
    elif modo == "�🔍 Consultar Questões":
        st.header("Banco de Questões SAEB")
        
        descritores = obter_descritores_unicos()
        questoes = listar_todas_questoes()
        
        # Filtrar por descritor
        descritor_selecionado = st.selectbox(
            "Filtrar por descritor:",
            descritores
        )
        
        questoes_filtradas = [q for q in questoes if q['descritor'] == descritor_selecionado]
        
        st.write(f"**{len(questoes_filtradas)} questão(ões) para {descritor_selecionado}**")
        
        for questao in questoes_filtradas:
            with st.expander(f"Q{questao['id']} - {questao['competencia'][:50]}..."):
                st.write(f"**Descritor:** {questao['descritor']}")
                st.write(f"**Competência:** {questao['competencia']}")
                st.write(f"**Tipo de texto:** {questao['tipo_texto']}")
                
                st.write("\n**Enunciado:**")
                st.write(questao['enunciado'])
                
                st.write("\n**Alternativas:**")
                for alt, texto in questao['alternativas'].items():
                    st.write(f"**{alt})** {texto}")
                
                st.write(f"\n**Resposta correta:** {questao['resposta_correta']}")
                st.write(f"**Justificativa:** {questao['justificativa']}")
    
    elif modo == "ℹ️ Sobre Descritores":
        st.header("Descritores SAEB - Português 9º Ano")
        
        st.info("Conheça os descritores avaliados nas questões SAEB de Português do 9º ano.")
        
        descritores_info = {
            "D1": {
                "titulo": "Localizar informações explícitas",
                "descricao": "Encontrar dados e informações que estão escritos diretamente no texto",
                "exemplo": "Quando uma questão pergunta 'Qual é o nome do personagem?' ou 'Em que ano aconteceu?'"
            },
            "D3": {
                "titulo": "Inferir ideia principal",
                "descricao": "Identificar o tema ou assunto central do texto",
                "exemplo": "Quando uma questão pergunta 'Sobre o quê é o texto?' ou 'Qual é o tema?'"
            },
            "D4": {
                "titulo": "Inferir informação implícita",
                "descricao": "Deduzir informações que estão 'nas entrelinhas' do texto",
                "exemplo": "Quando uma questão pergunta 'O que se conclui?' ou 'O que se deduz?'"
            },
            "D6": {
                "titulo": "Distinguir fato de opinião",
                "descricao": "Diferenciar fatos comprovados de opiniões pessoais",
                "exemplo": "Fato: '1500 foi quando... ' | Opinião: 'Acho que foi importante...'"
            },
            "D9": {
                "titulo": "Identificar causa e consequência",
                "descricao": "Reconhecer por que um evento causou outro",
                "exemplo": "Porque A aconteceu, então B aconteceu"
            },
            "D11": {
                "titulo": "Avaliar produção textual",
                "descricao": "Analisar se um texto está adequado ao gênero e propósito",
                "exemplo": "Avaliar se um texto narrativo tem os elementos corretos"
            },
            "D13": {
                "titulo": "Usar recursos coesivos",
                "descricao": "Identificar conexões entre partes do texto (pronomes, conectivos)",
                "exemplo": "Usar 'ele' ao invés de repetir o nome; usar 'portanto' para conectar ideias"
            },
            "D15": {
                "titulo": "Utilizar vocabulário apropriado",
                "descricao": "Usar palavras variadas e adequadas ao contexto",
                "exemplo": "Evitar repetir 'bom', usar 'excelente', 'magnífico', 'notável'"
            }
        }
        
        for cod, info in descritores_info.items():
            with st.expander(f"**{cod}** - {info['titulo']}"):
                st.write(f"**Descrição:** {info['descricao']}")
                st.write(f"**Exemplo:** {info['exemplo']}")

if __name__ == "__main__":
    main()
