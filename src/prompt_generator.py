"""
Gerador de Prompts para Questões de Múltipla Escolha SAEB
Cria prompts estruturados baseados em análise de respostas
"""

from src.questoes_saeb import obter_questao

class GeradorPromptsQuestoes:
    """Gera prompts otimizados para análise de questões SAEB por IAs modernas"""
    
    def __init__(self):
        pass
    
    def gerar_prompt_correcao_completa(self, analise_resultado):
        """
        Gera prompt completo para IA corrigir e explicar a questão
        
        Args:
            analise_resultado: Dict com resultado da análise
            
        Returns:
            String com prompt estruturado para IA
        """
        
        prompt = self._criar_cabecalho(analise_resultado)
        prompt += self._criar_contexto_questao(analise_resultado)
        prompt += self._criar_secao_instrucoes_correcao()
        
        return prompt
    
    def gerar_prompt_multiplas_questoes(self, analise_multipla):
        """
        Gera prompt para análise de conjunto de questões
        
        Args:
            analise_multipla: Dict com análise de múltiplas respostas
            
        Returns:
            String com prompt estruturado
        """
        prompt = self._criar_cabecalho_multiplo(analise_multipla)
        prompt += self._criar_contexto_multiplo(analise_multipla)
        prompt += self._criar_secao_instrucoes_relatorio()
        
        return prompt
    
    def gerar_prompt_rapido(self, questao_id, resposta_aluno):
        """Gera prompt rápido para análise imediata"""
        
        questao = obter_questao(questao_id)
        if not questao:
            return "Questão não encontrada"
        
        prompt = f"""# ANÁLISE DE RESPOSTA - QUESTÃO SAEB PORTUGUÊS 9º ANO

## Questão #{questao_id}
**Descritor:** {questao['descritor']} - {questao['competencia']}

**Enunciado:**
{questao['enunciado']}

**Alternativas:**
A) {questao['alternativas']['A']}
B) {questao['alternativas']['B']}
C) {questao['alternativas']['C']}
D) {questao['alternativas']['D']}

**Resposta do aluno:** {resposta_aluno}
**Resposta correta:** {questao['resposta_correta']}
**Justificativa:** {questao['justificativa']}

---

{self._criar_secao_instrucoes_correcao()}
"""
        return prompt
    
    def _criar_cabecalho(self, analise):
        """Cria cabecalho com informações da análise"""
        
        questao = obter_questao(analise["questao_id"])
        acertou = "✅ ACERTOU" if analise["acertou"] else "❌ ERROU"
        
        return f"""# ANÁLISE DE RESPOSTA - SAEB PORTUGUÊS 9º ANO

## Informações da Questão
- **ID:** {analise['questao_id']}
- **Descritor:** {analise['descritor']} - {analise['competencia']}
- **Tipo de texto:** {analise['tipo_texto']}
- **Resultado:** {acertou}

## Resposta do Aluno
- **Alternativa escolhida:** {analise['resposta_aluno']}
- **Resposta correta:** {analise['resposta_correta']}
- **Pontuação:** {analise['pontuacao']}/10

---

"""
    
    def _criar_cabecalho_multiplo(self, analise):
        """Cria cabecalho para análise de múltiplas questões"""
        
        total = analise["total_questoes"]
        acertos = analise["acertos"]
        percentual = analise["percentual_acerto"]
        
        return f"""# RELATÓRIO DE DESEMPENHO - QUESTÕES SAEB PORTUGUÊS 9º ANO

## Resumo Geral
- **Total de questões:** {total}
- **Acertos:** {acertos}
- **Erros:** {analise['erros']}
- **Percentual de acerto:** {percentual:.1f}%

## Análise por Descritor
- **Descritores com acerto total:** {', '.join(analise['descritores_fortes']) if analise['descritores_fortes'] else 'Nenhum'}
- **Descritores com algum erro:** {', '.join(analise['descritores_fraco']) if analise['descritores_fraco'] else 'Nenhum'}

---

"""
    
    def _criar_contexto_questao(self, analise):
        """Cria contexto detalhado da questão"""
        
        questao = obter_questao(analise["questao_id"])
        
        contexto = f"""## ENUNCIADO DA QUESTÃO

```
{questao['enunciado']}
```

## ALTERNATIVAS

A) {questao['alternativas']['A']}
B) {questao['alternativas']['B']}
C) {questao['alternativas']['C']}
D) {questao['alternativas']['D']}

## ANÁLISE DA RESPOSTA

**Resposta do aluno:** {analise['resposta_aluno']} - "{questao['alternativas'][analise['resposta_aluno']]}"
**Resposta correta:** {analise['resposta_correta']} - "{questao['alternativas'][analise['resposta_correta']]}"

**Justificativa oficial:** {questao['justificativa']}

## TIPO DE QUESTÃO
- **Descritor:** {analise['descritor']}
- **Competência:** {analise['competencia']}
- **Tipo de texto:** {analise['tipo_texto']}

## SUGESTÕES PARA RESPONDER CORRETAMENTE

"""
        
        for i, sugestao in enumerate(questao['sugestoes'], 1):
            contexto += f"{i}. {sugestao}\n"
        
        contexto += "\n---\n\n"
        return contexto
    
    def _criar_contexto_multiplo(self, analise):
        """Cria contexto para múltiplas questões"""
        
        contexto = "## QUESTÕES E RESPOSTAS\n\n"
        
        for resultado in analise["resultados_individuais"]:
            questao = obter_questao(resultado["questao_id"])
            status = "✅" if resultado["acertou"] else "❌"
            
            contexto += f"""### {status} Questão #{resultado['questao_id']} - {resultado['descritor']}
- Resposta do aluno: {resultado['resposta_aluno']}
- Resposta correta: {resultado['resposta_correta']}
- Justificativa: {resultado['justificativa']}

"""
        
        return contexto
    
    def _criar_secao_instrucoes_correcao(self):
        """Cria instruções de ouro para IA corrigir a questão"""
        
        return """---

## INSTRUÇÕES PARA GERAÇÃO DA ANÁLISE COMENTADA

Você está analisando a resposta de um(a) estudante do 9º ano a uma questão SAEB de Língua Portuguesa.

### SUA TAREFA:
Gere uma análise EDUCATIVA, COMENTADA e CONSTRUTIVA que:

### 1. ESTRUTURA (siga este formato)

```
[RESULTADO DA QUESTÃO]
[EXPLICAÇÃO DA RESPOSTA CORRETA]
[ANÁLISE DO ERRO (se houver)]
[ESTRATÉGIA PARA ACERTAR]
[EXEMPLO PRÁTICO]
[ORIENTAÇÕES FINAIS]
```

### 2. TOM OBRIGATÓRIO
- ✅ **EDUCATIVO:** Explique por que a resposta está correta/incorreta
- ✅ **CONSTRUTIVO:** Mostre caminhos de melhoria, não apenas erros
- ✅ **ESPECÍFICO:** Use a questão e as alternativas reais
- ✅ **OBJETIVO:** Sem generalizações, seja concreto
- ✅ **MOTIVADOR:** Reconheça dificuldade, mas mostre como melhorar

### 3. SEÇÕES OBRIGATÓRIAS

#### A) RESULTADO DA QUESTÃO
- Indique se acertou ou errou
- Se errou, mostre que aprender com erros é normal

#### B) EXPLICAÇÃO DA RESPOSTA CORRETA
- Por que a resposta correta está correta
- Cite trechos do texto/enunciado que justificam
- Explique a lógica por trás da resposta

#### C) ANÁLISE DO ERRO (apenas se errou)
- Explique por que a resposta escolhida está incorreta
- Identifique o "raciocínio errado" que pode ter levado a essa escolha
- NÃO seja crítico; seja pedagógico

#### D) ESTRATÉGIA PARA RESPONDER CORRETAMENTE
- Forneça passo a passo para resolver questões DESTE TIPO
- Relacione com o descritor e competência
- Dê dicas práticas

#### E) EXEMPLO PRÁTICO
- Crie um exemplo similar para praticar
- Ou cite outra questão semelhante

#### F) ORIENTAÇÕES FINAIS
- Resumo do aprendizado
- Próximos passos
- Encorajamento

### 4. REQUISITOS OBRIGATÓRIOS
- Linguagem clara e acessível (para jovem de 15 anos)
- Total: 800-1200 palavras
- Cite SEMPRE o descritor avaliado
- Explique O POR QUÊ de cada conceito
- Seja equilibrado: reconheça se acertou, mas mostre como melhorar
- Se errou, tome como oportunidade de aprendizagem

### 5. EXEMPLO DE RESPOSTA PARA QUESTÃO D1 (se acertou)
```
✅ PARABÉNS! Você acertou!

A resposta correta é a alternativa [X], e você identificou corretamente!

EXPLICAÇÃO:
A questão pedia para localizar informação EXPLÍCITA no texto...
[explicação detalhada com citações do texto]

DESCRITOR AVALIADO:
D1 - Localizar informações explícitas em um texto

Por que você acertou:
- Você procurou a informação no texto
- Você não confundiu com informações implícitas
- Respondeu baseado no que estava escrito, não em dedução

COMO CONTINUAR ACERTANDO QUESTÕES D1:
[passo a passo]
```

---

**AGORA GERE A ANÁLISE COMENTADA COMPLETA SEMPRE SEGUINDO ESSAS INSTRUÇÕES**
"""
    
    def _criar_secao_instrucoes_relatorio(self):
        """Cria instruções para relatório de múltiplas questões"""
        
        return """---

## INSTRUÇÕES PARA GERAR RELATÓRIO COMPLETO

Você está gerando um relatório educativo sobre o desempenho de um(a) estudante em questões SAEB.

### ESTRUTURA DO RELATÓRIO

1. **INTRODUÇÃO** - Resumir desempenho geral
2. **ANÁLISE POR QUESTÃO** - Análise individual de cada questão
3. **ANÁLISE POR DESCRITOR** - Agrupado por competências
4. **PONTOS FORTES** - O que o aluno fez bem
5. **PONTOS A MELHORAR** - Prioridades de estudo
6. **PLANO DE AÇÃO** - Próximos passos específicos

### TOM E ESTILO
- ✅ Educativo: explique cada conceito
- ✅ Construtivo: mais sugestões que críticas
- ✅ Objetivo: use dados e exemplos específicos
- ✅ Motivador: reconheça progressos, mesmo parciais
- ✅ Pedagógico: sempre ensiné, nunca apenas critique

### EXEMPLOS DE LINGUAGEM

**Para acertos:**
"Excelente! Você identificou corretamente porque..."

**Para erros:**
"Esta é uma questão desafiadora. Você escolheu X, mas a resposta correta é Y porque..."

**Para sugestões:**
"Para melhorar neste descritor, você pode..."

### REQUISITOS
- 1500-2500 palavras
- Estrutura clara com títulos
- Cite o descritor em cada análise
- Forneça exemplos práticos
- Inclua próximos passos específicos
- Seja motivador

---

**GERE AGORA O RELATÓRIO SEGUINDO TODAS AS INSTRUÇÕES ACIMA**
"""
