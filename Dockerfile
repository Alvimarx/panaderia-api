FROM python:3.12-slim

RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

# TEMPORALMENTE: ejecutar script de prueba en vez de FastAPI
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080} --log-level debug"]


