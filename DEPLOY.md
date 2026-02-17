# 🚀 Guia de Deploy no Streamlit Cloud

## Pré-requisitos
1. Conta GitHub (crie em github.com se não tiver)
2. Conta Streamlit Cloud (use GitHub para login)

## Passo 1: Preparar o repositório local

```bash
# Entrar na pasta do projeto
cd /home/sergio/analisador_saeb

# Inicializar git
git init

# Adicionar todos os arquivos
git add .

# Commit inicial
git commit -m "Analisador SAEB v1.0 - Deploy"
```

## Passo 2: Criar repositório no GitHub

1. Acesse https://github.com/new
2. Nome do repositório: `analisador-saeb`
3. Descrição: "App educacional para análise de questões SAEB de múltipla escolha com suporte a PDF, DOCX e OCR"
4. Escolha: **Public** (necessário para Streamlit Cloud)
5. Clique em "Create repository"

## Passo 3: Push para GitHub

Depois que o repositório for criado, o GitHub te mostrará os comandos. Execute:

```bash
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/analisador-saeb.git
git push -u origin main
```

(Substitua `SEU_USUARIO` pelo seu username do GitHub)

## Passo 4: Deploy no Streamlit Cloud

1. Acesse https://share.streamlit.io
2. Clique em "New app"
3. Preencha:
   - **Repository:** `SEU_USUARIO/analisador-saeb`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Clique em "Deploy"

## Passo 5: Acessar a aplicação

- Seu app estará disponível em: `https://analisador-saeb-RANDOM.streamlit.app`
- URL custom pode ser configurada posteriormente

## Estrutura esperada pelo Streamlit Cloud

✅ Arquivo `app.py` na raiz
✅ Arquivo `requirements.txt` com todas as dependências
✅ Pasta `src/` com módulos Python
✅ Arquivo `.gitignore` para excluir venv e cache

## Se encontrar problemas

### Erro: "Module not found"
- Verifique se `requirements.txt` tem todas as dependências
- Certifique-se que os imports estão corretos em `app.py`

### Erro com easyocr
- easyocr faz download de modelos (~200MB) na primeira execução
- Pode levar alguns minutos no deploy inicial
- Stream logs em "Manage app" → "Developer"

### OCR lento ou falhando
- Streamlit Cloud tem recursos limitados
- Para imagens muito grandes, considere reduzir tamanho

## Repositório Local vs Cloud

Depois do deploy inicial, qualquer `git push` para main atualiza automaticamente o app no Streamlit Cloud!

## Próximos passos (opcional)

1. **Secrets**: Para adicionar variáveis de ambiente no Streamlit Cloud
   - Manage app → Settings → Secrets
   - Copie conteúdo de `.streamlit/secrets.toml`

2. **Domínio custom**: Streamlit Cloud Pro permite domínios personalizados

3. **Monitoramento**: Use "Manage app" para ver logs e analytics

---

Boa sorte com o deploy! 🎉
