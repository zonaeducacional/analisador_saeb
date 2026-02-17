"""
Módulo de Análise de Questões de Múltipla Escolha SAEB
Corrige respostas e fornece feedback pedagógico
"""

from src.questoes_saeb import obter_questao, listar_todas_questoes, obter_questoes_por_descritor

class AnalisadorQuestoes:
    """Analisa respostas de questões SAEB de múltipla escolha"""
    
    def __init__(self):
        self.questoes = listar_todas_questoes()
    
    def analisar_resposta(self, id_questao, resposta_aluno):
        """
        Analisa a resposta de um aluno para uma questão específica
        
        Args:
            id_questao: ID da questão
            resposta_aluno: Alternativa escolhida (A, B, C ou D)
            
        Returns:
            Dict com análise completa da resposta
        """
        questao = obter_questao(id_questao)
        
        if not questao:
            return {
                "erro": "Questão não encontrada",
                "id_questao": id_questao
            }
        
        resposta_aluno = resposta_aluno.upper().strip() if resposta_aluno else ""
        
        # Validar resposta
        if resposta_aluno not in questao["alternativas"]:
            return {
                "erro": "Resposta inválida. Use A, B, C ou D",
                "questao_id": id_questao
            }
        
        # Analisar resposta
        acertou = resposta_aluno == questao["resposta_correta"]
        
        resultado = {
            "questao_id": id_questao,
            "descritor": questao["descritor"],
            "competencia": questao["competencia"],
            "enunciado": questao["enunciado"],
            "alternativas": questao["alternativas"],
            "resposta_aluno": resposta_aluno,
            "resposta_correta": questao["resposta_correta"],
            "acertou": acertou,
            "justificativa": questao["justificativa"],
            "tipo_texto": questao["tipo_texto"],
            "sugestoes_procedimentais": questao["sugestoes"],
            "feedback": self._gerar_feedback(acertou, questao, resposta_aluno),
            "pontuacao": 10 if acertou else 0
        }
        
        return resultado
    
    def _gerar_feedback(self, acertou, questao, resposta_aluno):
        """Gera feedback personalizado baseado no resultado"""
        
        if acertou:
            return f"""✅ PARABÉNS! Você acertou!

Você escolheu a alternativa {resposta_aluno}: "{questao['alternativas'][resposta_aluno]}"

Justificativa: {questao['justificativa']}

Você identificou corretamente o descritor {questao['descritor']} - {questao['competencia']}"""
        
        else:
            resposta_correta = questao["resposta_correta"]
            texto_resposta_correta = questao["alternativas"][resposta_correta]
            texto_sua_resposta = questao["alternativas"][resposta_aluno]
            
            return f"""❌ Sua resposta está incorreta.

Você escolheu: {resposta_aluno} - "{texto_sua_resposta}"
Resposta correta: {resposta_correta} - "{texto_resposta_correta}"

Explicação: {questao['justificativa']}

Descritor avaliado: {questao['descritor']} - {questao['competencia']}"""
    
    def obter_sugestoes_melhoria(self, id_questao):
        """Retorna sugestões pedagógicas para responder corretamente questões deste tipo"""
        questao = obter_questao(id_questao)
        
        if not questao:
            return None
        
        return {
            "descritor": questao["descritor"],
            "competencia": questao["competencia"],
            "tipo_questao": self._classificar_tipo_questao(questao["descritor"]),
            "sugestoes": questao["sugestoes"],
            "passo_a_passo": self._gerar_passo_a_passo(questao["descritor"]),
            "exemplos_pratica": self._gerar_exemplos(questao["descritor"])
        }
    
    def _classificar_tipo_questao(self, descritor):
        """Classifica o tipo de questão pelo descritor"""
        tipos = {
            "D1": "Localização de informação explícita",
            "D3": "Identificação de ideia principal",
            "D4": "Inferência de informação implícita",
            "D6": "Distinção entre fato e opinião",
            "D9": "Identificação de causa e consequência",
            "D11": "Avaliação de produção textual",
            "D13": "Análise de coesão",
            "D15": "Análise de vocabulário"
        }
        return tipos.get(descritor, "Questão de compreensão")
    
    def _gerar_passo_a_passo(self, descritor):
        """Gera estratégia passo a passo para responder questões deste tipo"""
        
        estrategias = {
            "D1": [
                "1. Leia o enunciado com atenção, procurando a pergunta específica",
                "2. Procure no texto a palavra ou informação mencionada na pergunta",
                "3. Encontre a resposta DIRETAMENTE no texto (não deduza)",
                "4. Compare a resposta encontrada com as alternativas",
                "5. Escolha a alternativa que corresponde exatamente ao texto"
            ],
            "D3": [
                "1. Leia o texto inteiro uma primeira vez",
                "2. Identifique a ideia que se repete ou que está em todo o texto",
                "3. Procure por palavras-chave que definem o assunto central",
                "4. Diferencie detalhes do tema principal (D1 encontra detalhes, D3 encontra o geral)",
                "5. Escolha a alternativa que resume o texto todo, não apenas uma parte"
            ],
            "D4": [
                "1. Leia o texto e observe detalhes que NÃO estão explícitos",
                "2. Procure por sinais (gestos, tom, atmosfera) que sugerem algo",
                "3. Use sua experiência de vida para deduzir o que virá",
                "4. Procure por pergunta com 'conclui-se', 'deduz-se', 'infere-se'",
                "5. A resposta está 'entre as linhas' do texto, não escrita exatamente"
            ],
            "D6": [
                "1. Identifique cada afirmação como fato ou opinião",
                "2. Fatos: são dados, números, datas, ações comprovadas",
                "3. Opiniões: contêm julgamentos, avaliações, 'acho que', 'é importante'",
                "4. Procure por indicadores de opinião: 'penso', 'acho', 'considero', 'ruim', 'bom'",
                "5. Fatos são verificáveis; opiniões dependem de ponto de vista"
            ],
            "D9": [
                "1. Identifique o PRIMEIRO evento (a causa inicial)",
                "2. Trace a sequência: o que acontece POR CAUSA de quê?",
                "3. Use conectivos como 'porque', 'como', 'portanto', 'então'",
                "4. Organize em ordem lógica (não cronológica necessariamente)",
                "5. Verifique se a sequência faz sentido: A causa B, B causa C, C causa D"
            ],
            "D11": [
                "1. Identifique qual é o gênero textual esperado",
                "2. Verifique se a estrutura está correta para esse gênero",
                "3. Procure por argumentos válidos (não apenas afirmações)",
                "4. Verifique se há exemplos, dados ou justificativas",
                "5. Avalie se a linguagem e tom são apropriados ao gênero"
            ],
            "D13": [
                "1. Procure por pronomes (ele, ela, seu, sua) que retomam pessoas/coisas",
                "2. Identifique conectivos (e, mas, portanto, além disso)",
                "3. Verifique se as ideias estão ligadas logicamente",
                "4. Procure por repetição inteligente de termos usando sinônimos",
                "5. O texto deve 'fluir' sem frases soltas desconectadas"
            ],
            "D15": [
                "1. Procure por repetição da mesma palavra",
                "2. Verifique se há sinônimos para variar o vocabulário",
                "3. Palavras genéricas ('coisa', 'bom', 'ruim') são mais fracas",
                "4. Palavras específicas e apropriadas melhoram a qualidade",
                "5. Evite repetição; use diferentes estruturas e termos"
            ]
        }
        
        return estrategias.get(descritor, ["Analise o tipo de questão especificamente"])
    
    def _gerar_exemplos(self, descritor):
        """Gera exemplos de prática para o descritor"""
        
        exemplos = {
            "D1": "Procure por questões que perguntam 'Onde?', 'Quando?', 'Quem?', 'Qual é?' - estas pedem informações diretas",
            "D3": "Questões que perguntam 'Sobre o quê?' ou 'Qual é o tema?' - procure a ideia geral",
            "D4": "Questões que perguntam 'O que se conclui?', 'O que se deduz?' - use pistas do texto",
            "D6": "Procure textos que misturam dados reais com avaliações pessoais",
            "D9": "Leia histórias em sequência lógica: por que uma ação causou outra",
            "D11": "Leia vários gêneros e analise se cada texto segue seu padrão",
            "D13": "Localize todos os pronomes e conectivos em um texto",
            "D15": "Compare dois textos: um repetitivo e outro com vocabulário variado"
        }
        
        return exemplos.get(descritor, "Continue praticando questões deste tipo")
    
    def analisar_multiplas_respostas(self, respostas_dict):
        """
        Analisa um conjunto de respostas
        
        Args:
            respostas_dict: Dict {id_questao: resposta_aluno, ...}
            
        Returns:
            Análise agregada
        """
        resultados = []
        acertos = 0
        total = 0
        
        for id_questao, resposta in respostas_dict.items():
            resultado = self.analisar_resposta(id_questao, resposta)
            if "erro" not in resultado:
                resultados.append(resultado)
                if resultado["acertou"]:
                    acertos += 1
                total += 1
        
        # Agrupar por descritor
        por_descritor = {}
        for r in resultados:
            desc = r["descritor"]
            if desc not in por_descritor:
                por_descritor[desc] = []
            por_descritor[desc].append(r)
        
        return {
            "total_questoes": total,
            "acertos": acertos,
            "erros": total - acertos,
            "percentual_acerto": (acertos / total * 100) if total > 0 else 0,
            "resultados_individuais": resultados,
            "analise_por_descritor": por_descritor,
            "descritores_fortes": [d for d, r in por_descritor.items() if all(x["acertou"] for x in r)],
            "descritores_fraco": [d for d, r in por_descritor.items() if any(not x["acertou"] for x in r)]
        }
