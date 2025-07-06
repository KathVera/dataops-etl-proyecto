FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Agrega esta línea para que Python reconozca /app como raíz
ENV PYTHONPATH=/app

CMD ["python", "main.py"]
