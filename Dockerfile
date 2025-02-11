# Utiliser une image Python légère
FROM python:3.9-slim

WORKDIR /app

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers du projet
COPY . .

# Définir le point d’entrée
CMD ["python", "train.py"]
