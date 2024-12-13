import zipfile
import rarfile
import os

# Demander les chemins d'accès
COMPRESSED_FOLDER = input("Entrez le chemin vers le dossier contenant les fichiers compressés : ").strip().strip('"')
EXTRACT_FOLDER = input("Entrez le chemin vers le dossier de destination : ").strip().strip('"')

# Normaliser les chemins pour éviter les problèmes
COMPRESSED_FOLDER = os.path.normpath(COMPRESSED_FOLDER)
EXTRACT_FOLDER = os.path.normpath(EXTRACT_FOLDER)

# Vérifier si les dossiers existent
if not os.path.exists(COMPRESSED_FOLDER):
    print(f"Erreur : Le dossier source '{COMPRESSED_FOLDER}' n'existe pas.")
    exit(1)

# Créer le dossier de destination s'il n'existe pas
os.makedirs(EXTRACT_FOLDER, exist_ok=True)

# Parcourir tous les fichiers dans le dossier compressé
for item in os.listdir(COMPRESSED_FOLDER):
    file_path = os.path.join(COMPRESSED_FOLDER, item)

    # Vérifier si c'est un fichier ZIP
    if item.lower().endswith('.zip'):
        print(f"Décompression de : {file_path} (ZIP)")
        try:
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                # Créer un sous-dossier pour chaque fichier ZIP
                student_folder = os.path.join(EXTRACT_FOLDER, os.path.splitext(item)[0])
                os.makedirs(student_folder, exist_ok=True)
                zip_ref.extractall(student_folder)
            print(f"Décompressé dans : {student_folder}")
        except zipfile.BadZipFile:
            print(f"Erreur : Le fichier ZIP {file_path} est corrompu ou invalide.")
        except Exception as e:
            print(f"Une erreur est survenue lors de la décompression de {file_path} : {e}")

    # Vérifier si c'est un fichier RAR
    elif item.lower().endswith('.rar'):
        print(f"Décompression de : {file_path} (RAR)")
        try:
            with rarfile.RarFile(file_path) as rar_ref:
                # Créer un sous-dossier pour chaque fichier RAR
                student_folder = os.path.join(EXTRACT_FOLDER, os.path.splitext(item)[0])
                os.makedirs(student_folder, exist_ok=True)
                rar_ref.extractall(student_folder)
            print(f"Décompressé dans : {student_folder}")
        except rarfile.BadRarFile:
            print(f"Erreur : Le fichier RAR {file_path} est corrompu ou invalide.")
        except rarfile.NeedFirstVolume:
            print(f"Erreur : Le fichier RAR {file_path} nécessite un volume supplémentaire.")
        except Exception as e:
            print(f"Une erreur est survenue lors de la décompression de {file_path} : {e}")

    else:
        print(f"Format de fichier non supporté : {file_path}")
