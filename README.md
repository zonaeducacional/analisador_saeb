# Corretor de Questões SAEB - Português 9º Ano

Aplicativo educacional para correção e análise de questões de múltipla escolha do SAEB (Sistema de Avaliação da Educação Básica), baseado nos descritores da prova de Língua Portuguesa do 9º ano.

## 🎯 Objetivo

Fornecer uma ferramenta que:
- ✅ Corrige respostas de questões SAEB de múltipla escolha
- ✅ Identifica qual descritor está sendo avaliado
- ✅ Explica a resposta correta respostas
- ✅ Gera prompts poderosos para IAs modernas
- ✅ Facilita feedback pedagógico construtivo e comentado
- ✅ Orienta alunos sobre como responder corretamente

## 🚀 Como Instalar e Executar

### Pré-requisitos
- Python 3.8 ou superior
- pip

### Passos

1. Clone ou navegue até o diretório do projeto:
```bash
cd analisador_saeb
```

2. O projeto já está configurado com dependências instaladas. Para reinstalar (se necessário):
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
streamlit run app.py
```

4. A aplicação será aberta em `http://localhost:8501`

## 📖 Como Usar

### Modo 1: Analisar uma Questão Individual
1. Selecione uma questão do banco
2. Leia o enunciado e as alternativas
3. Escolha sua resposta (A, B, C ou D)
4. Clique em "Analisar Resposta"
5. Revise o feedback:
   - Se acertou: parabéns e explicação da resposta correta
   - Se errou: explicação da resposta correta + por que sua resposta estava errada
6. Clique em "Gerar Prompt Completo"
7. Copie o prompt
8. Cole em ChatGPT, Claude ou outra IA moderna para obter análise detalhada

### Modo 2: Analisar Múltiplas Questões
1. Responda várias questões do banco
2. Clique em "Analisar Todas"
3. Obtenha análise agregada:
   - Taxa de acerto geral
   - Descritores (fortes e fracos)
   - Detalhes de cada questão
4. Gere prompt de relatório completo para a IA

### Modo 3: Consultar Questões
- Navegue pelo banco de questões
- Filtre por descritor
- Visualize enunciado, alternativas e resposta correta

### Modo 4: Sobre Descritores
- Aprenda sobre cada descritor SAEB
- Entenda o que cada competência avalia
- Veja exemplos de questões relacionadas

## 📊 Descritor es SAEB Avaliados

### D1 - Localizar informações explícitas
Encontrar dados e informações que estão escritos diretamente no texto

### D3 - Inferir ideia principal
Identificar o tema ou assunto central do texto

### D4 - Inferir informação implícita
Deduzir informações que estão "nas entrelinhas" do texto

### D6 - Distinguir fato de opinião
Diferenciar fatos comprovados de opiniões pessoais

### D9 - Identificar causa e consequência
Reconhecer por que um evento causou outro

### D11 - Avaliar produção textual
Analisar se um texto está adequado ao gênero e propósito

### D13 - Usar recursos coesivos
Identificar conexões entre partes do texto (pronomes, conectivos)

### D15 - Utilizar vocabulário apropriado
Usar palavras variadas e adequadas ao contexto

## 🤖 Geração de Prompts para IA

O app gera prompts otimizados que orientam IAs a:
- ✅ Explicar por que a resposta está correta/incorreta
- ✅ Citar exemplos específicos da questão
- ✅ Oferecer estratégias passo a passo
- ✅ Ser educativo e construtivo
- ✅ Fornecer exemplos práticos
- ✅ Criar orientações para acertar questões similares

### Instruções de Ouro para IA

Os prompts incluem instruções obrigatórias que pedem à IA para:
1. **Educar:** Explicar cada conceito de forma acessível
2. **Construir:** Mostrar caminhos de melhoria
3. **Especificar:** Usar exemplos concretos
4. **Objetivar:** Sem generalidades
5. **Motivar:** Reconhecer dificuldades e mostrar progresso

## 📁 Estrutura do Projeto

```
analisador_saeb/
├── app.py                    # App principal em Streamlit
├── requirements.txt          # Dependências
├── README.md                 # Este arquivo
├── src/
│   ├── __init__.py
│   ├── questoes_saeb.py      # Banco de 8+ questões SAEB
│   ├── analisador.py         # Lógica de análise de questões
│   └── prompt_generator.py   # Gerador de prompts para IA
├── .github/
│   └── copilot-instructions.md
└── .vscode/
    └── tasks.json            # Tasks VS Code
```

## 🔧 Características Técnicas

### Análise de Questões
- Valida alternativas (A, B, C, D)
- Compara com resposta correta
- Gera feedback personalizado
- Calcula taxa de acerto

### Identificação de Descritores
- Mapeia cada questão a um descritor SAEB
- Agrupa questões por competência
- Identifica descritores fortes/fracos

### Geração de Prompts
- Estrutura com contexto SAEB completo
- Instruções de ouro para as IAs
- Orientações sobre tom pedagógico
- Requisitos de análise comentada

### Banco de Questões
- 8 questões exemplo com descritores variados
- Fácil extensão para mais questões
- Suporte a diferentes tipos de texto

## 📊 Banco de Questões

O projeto inclui 8 questões de exemplo (/src/questoes_saeb.py):

1. **Q1 (D1)** - Localizar informação explícita em texto histórico
2. **Q2 (D3)** - Identificar tema central de poema
3. **Q3 (D4)** - Inferir informação implícita em narrativa
4. **Q4 (D6)** - Distinguir fatos de opiniões
5. **Q5 (D9)** - Identificar causa e consequência
6. **Q6 (D11)** - Avaliar argumentação em texto
7. **Q7 (D13)** - Criticar uso de pronomes e conectivos
8. **Q8 (D15)** - Analisar variedade de vocabulário

### Adicionar Novas Questões

Para adicionar novas questões, edite `/src/questoes_saeb.py` seguindo o template:

```python
{
    "id": 9,
    "descritor": "D1",
    "competencia": "Localizar informações explícitas em um texto",
    "enunciado": "Seu enunciado aqui...",
    "alternativas": {
        "A": "Opção A",
        "B": "Opção B",
        "C": "Opção C",
        "D": "Opção D"
    },
    "resposta_correta": "A",
    "justificativa": "Por que A está correta...",
    "tipo_texto": "Tipo de texto (narrativo, dissertativo, etc)",
    "sugestoes": [
        "Sugestão 1",
        "Sugestão 2",
        "Sugestão 3"
    ]
}
```

## 🎓 Fluxo de Uso Recomendado

### Para Professores/Educadores
1. Aluno responde uma questão SAEB
2. Você insere a resposta no app
3. O app fornece análise preliminar
4. Você clica em "Gerar Prompt"
5. Copia o prompt para ChatGPT/Claude
6. IA gera relatório comentado e construtivo
7. Você compartilha o relatório com o aluno

### Para Alunos
1. Responda a uma questão SAEB
2. Insira sua resposta no app
3. Receba feedback do app
4. Professor ou educador gera prompt para IA
5. Leia o relatório da IA
6. Entenda por que errou (ou acertou)
7. Aprenda estratégia para questões similares

### Ciclo de Aprendizado
1. **Responder:** Aluno responde várias questões
2. **Analisar:** App fornece feedback
3. **Entender:** IA explica via relatório comentado
4. **Refletir:** Aluno compreende o conceito
5. **Praticar:** Aluno tenta novamente

## 🔗 Integração com IAs Modernas

Os prompts gerados são compatíveis com:
- ✅ ChatGPT (GPT-4, GPT-3.5)
- ✅ Claude (Anthropic)
- ✅ Gemini (Google)
- ✅ Outras LLMs que suportam instruções estruturadas

## 📝 Exemplo de Saída

### Quando acerta:
```
✅ PARABÉNS! Você acertou!

Você escolheu: B - "Alcançar a Índia"

Justificativa: O texto afirma explicitamente: "a expedição tinha como objetivo inicial alcançar a Índia"

Você identificou corretamente o descritor D1 - Localizar informações explícitas
```

### Quando erra:
```
❌ Sua resposta está incorreta.

Você escolheu: A - "Conquistar o Brasil para Portugal"
Resposta correta: B - "Alcançar a Índia"

Explicação: O texto afirma explicitamente que o objetivo inicial era alcançar a Índia, não conquistar o Brasil...

Descritor avaliado: D1 - Localizar informações explícitas
```

## 🎯 Casos de Uso

### 1. Sala de Aula
- Professor usa para corrigir e explicar questões
- Alunos resolvem e recebem feedback automático

### 2. Reforço Escolar
- Educadores geram análises detalhadas
- Estudantes entendem conceitos através de exemplos

### 3. Preparação para SAEB
- Praticar questões similares às da prova
- Entender descritores e competências

### 4. Educação a Distância
- Ferramenta para autoavaliação
- Feedback personalizado sem intermediário

## 💡 Diferenciais

- 🎯 **Específico:** Foco exclusivo em questões SAEB de Português 9º ano
- 🤖 **IA-Ready:** Prompts otimizados para IAs modernas
- 📚 **Educativo:** Explica não apenas o que errou, mas por quê e como melhorar
- ♻️ **Reutilizável:** Mesmos prompts podem ser usados em qualquer IA
- 📊 **Analítico:** Identifica padrões de erros por descritor

## 🔄 Fluxo de Dados

```
Questão + Resposta do Aluno
        ↓
  AnalisadorQuestoes
  (Valida e compara)
        ↓
  Resultado + Feedback
        ↓
  GeradorPrompts
  (Cria instruções)
        ↓
  Prompt para IA
  (ChatGPT, Claude, etc)
        ↓
  Relatório Comentado
  (Educativo e construtivo)
```

## 🚧 Próximas Funcionalidades

- [ ] Banco de questões expandido (50+ questões)
- [ ] Histórico de desempenho por aluno
- [ ] Relatórios em PDF
- [ ] Integração com LMS (Moodle, Google Classroom)
- [ ] Suporte a outros idiomas
- [ ] Análise de padrões de erro

## 📞 Suporte

Para questões sobre:
- **Descritores SAEB:** Consulte [INEP/MEC](https://www.gov.br/inep)
- **Uso do app:** Verifique os modos disponíveis nas tabs
- **Prompts:** Revise as instruções na geração

## 📄 Licença

Este projeto é fornecido para fins educacionais.

---

**Versão:** 2.0 (Refatorada para Questões de Múltipla Escolha)  
**Data:** Fevereiro 2026  
**Status:** ✅ Funcional e testado
