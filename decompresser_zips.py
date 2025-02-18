import os
import zipfile
import rarfile
import tarfile
import py7zr
import time

# Demande des chemins source et destination
SOURCE_FOLDER = input("Entrez le chemin vers le dossier contenant les fichiers compressés : ").strip('"')
DEST_FOLDER = input("Entrez le chemin vers le dossier de destination : ").strip('"')

# Normalisation des chemins
SOURCE_FOLDER = os.path.normpath(SOURCE_FOLDER)
DEST_FOLDER = os.path.normpath(DEST_FOLDER)

# Vérifier l'existence du dossier source
if not os.path.exists(SOURCE_FOLDER):
    print(f"Erreur : Le dossier source '{SOURCE_FOLDER}' n'existe pas.")
    exit(1)

# Créer le dossier de destination s'il n'existe pas
os.makedirs(DEST_FOLDER, exist_ok=True)

def extract_file(file_path, destination_folder, remove_archive=True):
    """
    Extrait une archive (ZIP, RAR, TAR ou 7z) depuis file_path dans destination_folder.
    le fichier archive est supprimé après extraction.
    """
    # Format ZIP
    if file_path.lower().endswith('.zip'):
        print(f"Décompression de : {file_path} (ZIP)")
        try:
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(destination_folder)
            time.sleep(0.1)
            if remove_archive:
                os.remove(file_path)
                print(f"Supprimé : {file_path}")
        except zipfile.BadZipFile:
            print(f"Erreur : Le fichier ZIP {file_path} est corrompu ou invalide.")
        except Exception as e:
            print(f"Erreur lors de la décompression de {file_path} : {e}")

    # Format RAR
    elif file_path.lower().endswith('.rar'):
        print(f"Décompression de : {file_path} (RAR)")
        try:
            with rarfile.RarFile(file_path) as rar_ref:
                rar_ref.extractall(destination_folder)
            if remove_archive:
                os.remove(file_path)
                print(f"Supprimé : {file_path}")
        except rarfile.BadRarFile:
            print(f"Erreur : Le fichier RAR {file_path} est corrompu ou invalide.")
        except Exception as e:
            print(f"Erreur lors de la décompression de {file_path} : {e}")

    # Format TAR (et variantes : .tar.gz, .tgz, .tar.bz2, .tbz2)
    elif file_path.lower().endswith(('.tar', '.tar.gz', '.tgz', '.tar.bz2', '.tbz2')):
        print(f"Décompression de : {file_path} (TAR)")
        try:
            with tarfile.open(file_path, 'r:*') as tar:
                tar.extractall(destination_folder)
            time.sleep(0.1)
            if remove_archive:
                os.remove(file_path)
                print(f"Supprimé : {file_path}")
        except Exception as e:
            print(f"Erreur lors de la décompression de {file_path} : {e}")

    # Format 7z
    elif file_path.lower().endswith('.7z'):
        print(f"Décompression de : {file_path} (7z)")
        try:
            with py7zr.SevenZipFile(file_path, mode='r') as archive:
                archive.extractall(path=destination_folder)
            time.sleep(0.1)
            if remove_archive:
                os.remove(file_path)
                print(f"Supprimé : {file_path}")
        except Exception as e:
            print(f"Erreur lors de la décompression de {file_path} : {e}")

    else:
        print(f"Format non pris en charge pour le fichier : {file_path}")

def process_nested_archives(folder):
    """
    Parcourt récursivement le dossier 'folder' pour y décompresser les archives imbriquées.
    """
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        # Si c'est une archive, on crée un sous-dossier et on l'extrait dedans
        if os.path.isfile(item_path) and item_path.lower().endswith(('.zip', '.rar', '.tar', '.tar.gz', '.tgz', '.tar.bz2', '.tbz2', '.7z')):
            nested_folder = os.path.join(folder, os.path.splitext(item)[0])
            os.makedirs(nested_folder, exist_ok=True)
            extract_file(item_path, nested_folder, remove_archive=True)
            # Traitement récursif dans le dossier extrait (pour des archives imbriquées à plusieurs niveaux)
            process_nested_archives(nested_folder)
        # Sinon, si c'est un dossier, on descend dedans
        elif os.path.isdir(item_path):
            process_nested_archives(item_path)

# Pour chaque archive trouvée, on calcule son chemin relatif pour recréer la même structure dans le dossier de destination.
for root, dirs, files in os.walk(SOURCE_FOLDER):
    for file in files:
        if file.lower().endswith(('.zip', '.rar', '.tar', '.tar.gz', '.tgz', '.tar.bz2', '.tbz2', '.7z')):
            archive_path = os.path.join(root, file)
            # Chemin relatif depuis le dossier source
            relative_dir = os.path.relpath(root, SOURCE_FOLDER)
            # Dans le dossier de destination, on crée le même chemin, puis un sous-dossier portant le nom de l'archive
            extraction_dir = os.path.join(DEST_FOLDER, relative_dir, os.path.splitext(file)[0])
            os.makedirs(extraction_dir, exist_ok=True)
            # Extraction de l'archive depuis le dossier source vers le dossier de destination
            # On ne supprime PAS l'archive source (remove_archive=False)
            extract_file(archive_path, extraction_dir, remove_archive=False)
            # On traite les archives imbriquées dans le contenu extrait
            process_nested_archives(extraction_dir)

print("Décompression terminée.")
print(f"Les fichiers décompressés se trouvent dans '{DEST_FOLDER}'.")
