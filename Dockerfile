# Usamos la imagen oficial de Python 3.10 como base
FROM python:3.10-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código de la carpeta actual al contenedor
COPY . .

# Comando para ejecutar el script principal ETL
CMD ["python", "etl/main.py"]
