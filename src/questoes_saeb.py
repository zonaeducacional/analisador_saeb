"""
Banco de Questões SAEB - Português 9º Ano
Questões de múltipla escolha com descritores
"""

QUESTOES_SAEB = [
    {
        "id": 1,
        "descritor": "D1",
        "competencia": "Localizar informações explícitas em um texto",
        "enunciado": """Leia o texto abaixo:

"No ano de 1500, uma frota portuguesa comandada por Pedro Álvares Cabral aportou nas terras que 
seria chamadas Brasil. Com mais de 1.200 homens e 13 embarcações, a expedição tinha como objetivo 
inicial alcançar a Índia, mas foi desviada pela corrente marina."

Qual foi o principal objetivo inicial da expedição de Pedro Álvares Cabral?""",
        "alternativas": {
            "A": "Conquistar o Brasil para Portugal",
            "B": "Alcançar a Índia",
            "C": "Explorar o continente americano",
            "D": "Estabelecer comércio com povos nativos"
        },
        "resposta_correta": "B",
        "justificativa": "O texto afirma explicitamente: 'a expedição tinha como objetivo inicial alcançar a Índia'",
        "tipo_texto": "Narrativo histórico",
        "sugestoes": [
            "Leia o texto com atenção buscando informações diretas",
            "Procure por palavras-chave como 'objetivo', 'meta', 'propósito'",
            "Respostas diretas e explícitas no texto indicam questões D1",
            "Não confunda 'objetivo inicial' com 'resultado final'"
        ]
    },
    {
        "id": 2,
        "descritor": "D3",
        "competencia": "Inferir a ideia principal ou informação central de um texto",
        "enunciado": """Leia o poema abaixo:

"Há um menino
Há um moleque
Morando sempre esse meu quintal...

Toda vez que a gente brinca
Na rua, na chuva fazendo lama
Meu pai fica bravo
Meu pai fica triste
Meu pai fica... seco."

Qual é o tema central deste poema?""",
        "alternativas": {
            "A": "Um menino brincando na chuva",
            "B": "A relação conflituosa entre pai e filho",
            "C": "As brincadeiras de criança na rua",
            "D": "O sentimento de culpa em relação ao pai"
        },
        "resposta_correta": "B",
        "justificativa": "O poema retrata a tensão entre as brincadeiras infantis naturais e a reação negativa do pai, mostrando o conflito entre essas duas realidades.",
        "tipo_texto": "Poesia",
        "sugestoes": [
            "Identifique a mensagem geral, não apenas detalhes específicos",
            "Procure por sentimentos e emoções repetidas no texto",
            "A ideia principal abrange todo o texto, não apenas uma parte",
            "Questões D3 pedem 'tema', 'assunto', 'sobre o quê' o texto fala"
        ]
    },
    {
        "id": 3,
        "descritor": "D4",
        "competencia": "Inferir uma informação implícita em um texto",
        "enunciado": """Leia o texto:

"Mariana chegou em casa cansada. Tirou os sapatos, deixou a mochila no chão e caiu na poltrona. 
Sua mãe apareceu na porta com as mãos na cintura. Os olhos dela brilhavam de uma forma estranha. 
Mariana fechou os olhos e suspirou fundo."

O que pode ser inferido sobre o que vai acontecer?""",
        "alternativas": {
            "A": "Mariana vai dormir porque está cansada",
            "B": "A mãe vai sair de casa",
            "C": "Mariana vai discutir com sua mãe",
            "D": "Mariana vai fazer o dever de casa"
        },
        "resposta_correta": "C",
        "justificativa": "As pistas 'mãos na cintura', 'olhos brilhando de uma forma estranha' e o suspiro de Mariana indicam que há uma discussão iminente.",
        "tipo_texto": "Narrativo",
        "sugestoes": [
            "Procure por pistas sutis no texto (gestos, tons, atmosfera)",
            "Use sua experiência para deduzir o que virá",
            "Questões D4 usam palavras como 'deduz-se', 'conclui-se', 'infere-se'",
            "O que não está dito graficamente, mas 'lido nas entrelinhas'"
        ]
    },
    {
        "id": 4,
        "descritor": "D6",
        "competencia": "Distinguir um fato de uma opinião relativa a esse fato",
        "enunciado": """Leia as afirmações abaixo sobre o aquecimento global:

I. "A temperatura média do planeta aumentou 1°C desde o século XIX"
II. "O aquecimento global é o maior problema do planeta"
III. "As emissões de CO2 aumentaram 40% nos últimos 50 anos"
IV. "É impossível reverter os danos do aquecimento global"

Qual alternativa contém APENAS fatos?""",
        "alternativas": {
            "A": "I e III",
            "B": "II e IV",
            "C": "I e II",
            "D": "III e IV"
        },
        "resposta_correta": "A",
        "justificativa": "I e III apresentam dados mensuráveis. II é opinião ('maior problema'). IV é opinião ('impossível').",
        "tipo_texto": "Texto informativo",
        "sugestoes": [
            "Fatos: acontecimentos reais, dados, números, eventos comprovados",
            "Opiniões: julgamentos, avaliações, pontos de vista pessoais",
            "Palavras como 'acho', 'penso', 'é importante' indicam opinião",
            "Datas, números, ações concretas indicam fatos"
        ]
    },
    {
        "id": 5,
        "descritor": "D9",
        "competencia": "Identificar relação de causa e consequência entre partes do texto",
        "enunciado": """Leia:

"Como não havia chovido durante três meses, o rio da região secou completamente. 
Sem água, os agricultores não conseguiam irrigar suas plantações. 
As colheitas falharam e muitas famílias perderam suas fontes de renda."

Qual é a sequência de causa e consequência no texto?""",
        "alternativas": {
            "A": "Falta de chuva → rio seca → plantações falharam → famílias perderam renda",
            "B": "Famílias perderam renda → plantações falharam → rio secou → falta de chuva",
            "C": "Rio seca → falta de chuva → plantações falharam → famílias perderam renda",
            "D": "Plantações falharam → rio seca → falta de chuva → famílias perderam renda"
        },
        "resposta_correta": "A",
        "justificativa": "A sequência lógica é: a falta de chuva (causa inicial) secou o rio, o que impediu irrigação, causando falha nas colheitas e perda de renda.",
        "tipo_texto": "Texto explicativo",
        "sugestoes": [
            "Identifique o primeiro evento (causa primeira)",
            "Segue uma sequência de efeitos em cadeia",
            "Use conectivos como 'porque', 'como', 'portanto' como pistas",
            "Organize os eventos em ordem causal, não cronológica"
        ]
    },
    {
        "id": 6,
        "descritor": "D11",
        "competencia": "Produzir texto adequado ao gênero e propósito comunicativo",
        "enunciado": """Observe esta produção de um aluno:

"A multa por excesso de velocidade é ruim. É ruim porque prejudica o bolso da gente. 
Além disso, o trânsito é perigoso e as multas existem mesmo."

Qual crítica é mais apropriada para esta produção?""",
        "alternativas": {
            "A": "O texto tem muitos erros de pontuação",
            "B": "O texto não apresenta argumentos adequados para persuadir",
            "C": "O texto não tem informações sobre multas",
            "D": "O texto precisa de mais parágrafos"
        },
        "resposta_correta": "B",
        "justificativa": "Em um texto dissertativo-argumentativo, 'é ruim' não é argumento válido. São apenas afirmações repetidas sem justificativa sólida.",
        "tipo_texto": "Análise de produção textual",
        "sugestoes": [
            "Argumentos válidos: dados, exemplos, citações, lógica",
            "Afirmações sem base: repetição, opinião sem fundamentação",
            "Em textos argumentativos, cada ideia deve ser sustentada",
            "Use 'porque', 'pois', 'já que' para explicar razões reais"
        ]
    },
    {
        "id": 7,
        "descritor": "D13",
        "competencia": "Usar adequadamente recursos coesivos",
        "enunciado": """Leia:

"João e Maria foram à praia. _____ ficaram na água por horas. _____ voltaram para casa cansados."

Qual par de conectivos melhor completa as lacunas?""",
        "alternativas": {
            "A": "Eles / Portanto",
            "B": "Ambos / Depois",
            "C": "Eles / Depois",
            "D": "Ambos / Todavia"
        },
        "resposta_correta": "A",
        "justificativa": "'Eles' retoma anafórico os sujeitos, e 'Portanto' introduz conclusão lógica sobre o cansaço.",
        "tipo_texto": "Análise de coesão",
        "sugestoes": [
            "Pronomes (ele, ela, eles) substituem nomes anteriores",
            "Conectivos como 'portanto', 'logo' indicam conclusão",
            "Conectivos como 'mas', 'porém' indicam contraste",
            "Leia o contexto para entender qual conectivo faz sentido"
        ]
    },
    {
        "id": 8,
        "descritor": "D15",
        "competencia": "Utilizar vocabulário apropriado e variado",
        "enunciado": """Qual frase apresenta MELHOR vocabulário variado e apropriado?""",
        "alternativas": {
            "A": "A comida era boa. A bebida era boa. A companhia era boa. Tudo era muito bom.",
            "B": "A refeição era deliciosa. A bebida refrescante. A companhia agradável. Uma noite inesquecível.",
            "C": "A comida era boa. A bebida era divertida. A companhia era divertida. Tudo era muito bom.",
            "D": "Comida boa. Bebida boa. Companhia boa. Muito bom."
        },
        "resposta_correta": "B",
        "justificativa": "Usa vocabulário variado ('deliciosa', 'refrescante', 'agradável', 'inesquecível') e estruturas diferentes, evitando repetição.",
        "tipo_texto": "Análise de vocabulário",
        "sugestoes": [
            "Evite repetir a mesma palavra (ex: 'bom' repetido)",
            "Use sinônimos para variar o vocabulário",
            "Palavras mais específicas são melhores que genéricas",
            "A repetição dificulta a leitura e empobrece o texto"
        ]
    }
]

def obter_questao(id_questao):
    """Retorna uma questão específica"""
    for q in QUESTOES_SAEB:
        if q["id"] == id_questao:
            return q
    return None

def obter_questoes_por_descritor(descritor):
    """Retorna questões de um descritor específico"""
    return [q for q in QUESTOES_SAEB if q["descritor"] == descritor]

def listar_todas_questoes():
    """Lista todas as questões"""
    return QUESTOES_SAEB

def obter_descritores_unicos():
    """Retorna lista de descritores únicos"""
    return sorted(list(set(q["descritor"] for q in QUESTOES_SAEB)))
