# Imagen base oficial de Python
FROM python:3.12-slim

# Instala dependencias del sistema necesarias
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

# Establece el directorio de trabajo
WORKDIR /app

# Copia los requerimientos e instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación
COPY app ./app

# Comando para ejecutar la app con logs detallados
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--log-level", "debug"]
