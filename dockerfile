# Imagen base oficial de Python
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia requirements y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente
COPY app ./app

# Comando por defecto: ejecuta FastAPI con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
