FROM python:3.9

RUN pip install pyinstaller

# Copier le script 
COPY decompresser_zips.py /app/

# Générer l'exécutable Linux
RUN pyinstaller --onefile /app/decompresser_zips.py

# Définir le dossier de sortie
WORKDIR /app/dist

# affiche le chemin de l’exécutable
CMD ["ls", "-lh"]
