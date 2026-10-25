FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código y modelo
COPY api.py .
COPY modelo_propinas.pkl .

# Exponer puerto de FastAPI
EXPOSE 8000

# Comando para correr la API
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
