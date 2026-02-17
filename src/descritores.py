"""
Descritores e Competências do SAEB - Português 9º Ano
Base de dados com os descritores da avaliação
"""

DESCRITORES_SAEB = {
    "LEITURA_E_COMPREENSAO": {
        "D1": {
            "codigo": "D1",
            "descricao": "Localizar informações explícitas em um texto",
            "competencia": "Localizar informações manifestas em diferentes tipos de textos",
            "exemplos": [
                "Identificar dados específicos em notícias, relatórios ou narrativas",
                "Encontrar datas, nomes, números mencionados diretamente no texto"
            ]
        },
        "D2": {
            "codigo": "D2",
            "descricao": "Inferir o sentido de uma palavra ou expressão",
            "competencia": "Compreender o significado de vocábulos pelo contexto",
            "exemplos": [
                "Deduzir o sentido de palavras desconhecidas pela leitura",
                "Reconhecer sinonímia em expressões contextualizadas"
            ]
        },
        "D3": {
            "codigo": "D3",
            "descricao": "Inferir a ideia principal ou a informação central de um texto",
            "competencia": "Identificar o tema ou assunto central",
            "exemplos": [
                "Resumir em uma frase o tema de um parágrafo",
                "Identificar sobre o que essencialmente fala o texto"
            ]
        },
        "D4": {
            "codigo": "D4",
            "descricao": "Inferir uma informação implícita em um texto",
            "competencia": "Compreender informações que não estão ditas explicitamente",
            "exemplos": [
                "Deduzir motivos de personagens pelas ações descritas",
                "Reconhecer causas de eventos não mencionadas diretamente"
            ]
        },
        "D5": {
            "codigo": "D5",
            "descricao": "Identificar o tema ou assunto de um texto",
            "competencia": "Reconhecer o assunto central do texto",
            "exemplos": [
                "Classificar o tema de um texto em categorias específicas",
                "Nomear o assunto principal em diferentes gêneros textuais"
            ]
        },
        "D6": {
            "codigo": "D6",
            "descricao": "Distinguir um fato de uma opinião relativa a esse fato",
            "competencia": "Diferenciar fatos de opiniões",
            "exemplos": [
                "Separar afirmações verificáveis de interpretações pessoais",
                "Reconhecer argumentos pessoais em textos persuasivos"
            ]
        },
        "D7": {
            "codigo": "D7",
            "descricao": "Identificar o gênero de um texto",
            "competencia": "Reconhecer diferentes gêneros textuais",
            "exemplos": [
                "Classificar texto como notícia, conto, poema, carta etc",
                "Reconhecer características de cada gênero textual"
            ]
        },
        "D8": {
            "codigo": "D8",
            "descricao": "Identificar a finalidade de um texto",
            "competencia": "Reconhecer a intenção/propósito do texto",
            "exemplos": [
                "Reconhecer se é texto informativo, persuasivo ou emotivo",
                "Identificar para que foi escrito o texto"
            ]
        },
        "D9": {
            "codigo": "D9",
            "descricao": "Identificar a relação de causa e consequência entre partes e elementos do texto",
            "competencia": "Reconhecer relações lógicas entre eventos",
            "exemplos": [
                "Apontar por que algo aconteceu no texto",
                "Ligar eventos em sequência de causalidade"
            ]
        },
        "D10": {
            "codigo": "D10",
            "descricao": "Identificar o propósito comunicativo em diferentes gêneros",
            "competencia": "Reconhecer a intenção comunicativa",
            "exemplos": [
                "Distinguir comunicar, persuadir, emocionar, instruir",
                "Identificar quem fala e para quem em diferentes contextos"
            ]
        }
    },
    "PRODUCAO_TEXTUAL": {
        "D11": {
            "codigo": "D11",
            "descricao": "Produzir um texto adequado ao gênero e ao propósito comunicativo",
            "competencia": "Adequação do texto ao gênero solicitado",
            "exemplos": [
                "Escrever uma notícia respeitando estrutura de pirâmide invertida",
                "Produzir um conto com elementos de narrativa definidos"
            ]
        },
        "D12": {
            "codigo": "D12",
            "descricao": "Utilizar estratégias de organização textual apropriadas",
            "competencia": "Organização e estrutura lógica do texto",
            "exemplos": [
                "Dividirem parágrafos de forma coerente",
                "Usar conectivos para ligar ideias logicamente"
            ]
        },
        "D13": {
            "codigo": "D13",
            "descricao": "Usar adequadamente recursos coesivos",
            "competencia": "Coesão entre períodos e parágrafos",
            "exemplos": [
                "Empregar pronomes para retomar antecedentes",
                "Usar conectivos como 'portanto', 'contudo', 'além disso'"
            ]
        },
        "D14": {
            "codigo": "D14",
            "descricao": "Construir argumentação adequada ao propósito do texto",
            "competencia": "Argumentação e persuasão",
            "exemplos": [
                "Defender ponto de vista com argumentos válidos",
                "Usar exemplos e evidências para sustentar posição"
            ]
        },
        "D15": {
            "codigo": "D15",
            "descricao": "Utilizar vocabulário apropriado e variado",
            "competencia": "Repertório vocabular adequado",
            "exemplos": [
                "Evitar repetição excessiva de palavras",
                "Usar sinônimos e termos específicos do contexto"
            ]
        },
        "D16": {
            "codigo": "D16",
            "descricao": "Aplicar as convenções da escrita norma culta",
            "competencia": "Correção ortográfica e gramatical",
            "exemplos": [
                "Usar corretamente ortografia, pontuação e acentuação",
                "Respeitar concordância verbal e nominal"
            ]
        }
    }
}

def obter_descritores_por_categoria(categoria):
    """Retorna descritores de uma categoria específica"""
    return DESCRITORES_SAEB.get(categoria, {})

def obter_descritor(codigo):
    """Retorna um descritor específico pelo código"""
    for categoria in DESCRITORES_SAEB.values():
        if codigo in categoria:
            return categoria[codigo]
    return None

def listar_todas_categorias():
    """Lista todas as categorias de descritores"""
    return list(DESCRITORES_SAEB.keys())

def listar_todos_descritores():
    """Lista todos os descritores disponíveis"""
    descritores = []
    for categoria, itens in DESCRITORES_SAEB.items():
        for codigo, dados in itens.items():
            dados_copia = dados.copy()
            dados_copia['categoria'] = categoria
            descritores.append(dados_copia)
    return descritores
