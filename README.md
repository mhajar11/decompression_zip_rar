
# Décompresseur Automatique

## Description
Ce projet permet de décompresser automatiquement des fichiers (zip , rar , tar et 7z ) dans un dossier de destination spécifié.

## Instructions d'Utilisation

1. **Préparation des fichiers compressés :**
   - Téléchargez tous vos fichiers ZIP et (RAR , tar ou 7z )dans un même dossier.

2. **Utilisation de l'exécutable :**
   - Téléchargez l'exécutable généré dans le dossier `dist/`.
   - Double-cliquez sur le fichier `decompresser_zips.exe` pour l'exécuter.

3. **Configurer les chemins d'accès :**
     # Chemin vers le dossier contenant les fichiers compressés
     COMPRESSED_FOLDER = 'chemin/vers/votre/dossier/source'
     
     # Chemin vers le dossier de destination
     EXTRACT_FOLDER = 'chemin/vers/votre/dossier/destination'


## Remarques
- **Compatibilité des formats :**
  Ce projet prend en charge les fichiers compressés aux formats suivants :
  - `.zip`
  - `.rar`
  - `.tar`
  - `.7z`

- **Dépendances :**
exécuter : pip install -r requirements.txt

  Si vous exécutez le script Python directement, assurez-vous que les bibliothèques suivantes sont installées :
  - `zipfile` (inclus avec Python)
  - `rarfile` (à installer avec `pip install rarfile`)
  _ `py7zr`  (à installer avec `pip install py7zr`)

## Auteur
MHAJAR Youness

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.

