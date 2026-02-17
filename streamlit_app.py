"""
Aplicação Streamlit para Streamlit Cloud
Redireciona para o app.py principal
"""
import subprocess
import sys

# Executar o app.py
if __name__ == "__main__":
    subprocess.run([sys.executable, "app.py"])
