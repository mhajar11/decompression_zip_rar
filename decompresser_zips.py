import zipfile
import rarfile
import os
import time

COMPRESSED_FOLDER = input("Entrez le chemin vers le dossier contenant les fichiers compressés : ").strip('"')
EXTRACT_FOLDER = input("Entrez le chemin vers le dossier de destination : ").strip('"')

# Normaliser les chemins pour éviter les problèmes
COMPRESSED_FOLDER = os.path.normpath(COMPRESSED_FOLDER)
EXTRACT_FOLDER = os.path.normpath(EXTRACT_FOLDER)

# Vérifier si les dossiers existent
if not os.path.exists(COMPRESSED_FOLDER):
    print(f"Erreur : Le dossier source '{COMPRESSED_FOLDER}' n'existe pas.")
    exit(1)

# Créer le dossier de destination s'il n'existe pas
os.makedirs(EXTRACT_FOLDER, exist_ok=True)

def extract_file(file_path, destination_folder):
    """
    Fonction pour extraire un fichier compressé (ZIP ou RAR) dans un dossier donné,
    et supprimer le fichier compressé après extraction.
    """
    # Vérifier si c'est un fichier ZIP
    if file_path.lower().endswith('.zip'):
        print(f"Décompression de : {file_path} (ZIP)")
        try:
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                # Extraire dans le dossier
                zip_ref.extractall(destination_folder)
                print(f"Décompressé dans : {destination_folder}")

            # Attendre une petite pause pour s'assurer que le fichier est fermé
            time.sleep(0.1)

            # Vérifier s'il y a des fichiers ZIP dans les fichiers extraits
            for item in os.listdir(destination_folder):
                extracted_path = os.path.join(destination_folder, item)
                if item.lower().endswith('.zip'):
                    # Créer un sous-dossier pour le fichier ZIP imbriqué
                    nested_folder = os.path.join(destination_folder, os.path.splitext(item)[0])
                    os.makedirs(nested_folder, exist_ok=True)
                    extract_file(extracted_path, nested_folder)

            # Supprimer le fichier ZIP après extraction
            os.remove(file_path)
            print(f"Supprimé : {file_path}")

        except zipfile.BadZipFile:
            print(f"Erreur : Le fichier ZIP {file_path} est corrompu ou invalide.")
        except Exception as e:
            print(f"Une erreur est survenue lors de la décompression de {file_path} : {e}")

    # Vérifier si c'est un fichier RAR
    elif file_path.lower().endswith('.rar'):
        print(f"Décompression de : {file_path} (RAR)")
        try:
            with rarfile.RarFile(file_path) as rar_ref:
                rar_ref.extractall(destination_folder)
                print(f"Décompressé dans : {destination_folder}")

            # Supprimer le fichier RAR après extraction
            os.remove(file_path)
            print(f"Supprimé : {file_path}")

        except rarfile.BadRarFile:
            print(f"Erreur : Le fichier RAR {file_path} est corrompu ou invalide.")
        except rarfile.NeedFirstVolume:
            print(f"Erreur : Le fichier RAR {file_path} nécessite un volume supplémentaire.")
        except Exception as e:
            print(f"Une erreur est survenue lors de la décompression de {file_path} : {e}")


# Parcourir tous les fichiers dans le dossier compressé
for item in os.listdir(COMPRESSED_FOLDER):
    file_path = os.path.join(COMPRESSED_FOLDER, item)
    student_folder = os.path.join(EXTRACT_FOLDER, os.path.splitext(item)[0])

    # Créer un sous-dossier pour chaque fichier compressé
    os.makedirs(student_folder, exist_ok=True)

    # Extraire le fichier (ZIP ou RAR)
    extract_file(file_path, student_folder)
