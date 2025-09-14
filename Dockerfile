# Use uma imagem base oficial do Python.
# 'slim-buster' é uma versão menor e mais segura.
FROM python:3.9-slim-buster

# Define o diretório de trabalho dentro do container.
# Todas as instruções seguintes serão executadas a partir daqui.
WORKDIR /app

# Copia o arquivo da sua calculadora para o diretório de trabalho.
# O ponto (.) no final indica que o arquivo será copiado para o WORKDIR.
COPY calculadora.py .

# Comando que será executado quando o container for iniciado.
# Roda o script da calculadora.
CMD ["python", "calculadora.py"]
