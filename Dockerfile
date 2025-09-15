
FROM python:3.9-slim-buster


WORKDIR /app

COPY calculadora.py .


CMD ["python", "calculadora.py"]
