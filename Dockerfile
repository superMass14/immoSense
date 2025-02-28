FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Port à exposer
EXPOSE 5000

# Utiliser Gunicorn comme serveur WSGI pour la production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
