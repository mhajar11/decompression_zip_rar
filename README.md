<<<<<<< HEAD
# Décompresseur Automatique

## Description
Ce projet permet de décompresser des fichiers ZIP et RAR automatiquement.

## Utilisation
-changer ces lignes de codes: 
# Chemin vers le dossier contenant les fichiers compressés
COMPRESSED_FOLDER = ''  

# Chemin vers le dossier de destination
EXTRACT_FOLDER = ''

- Téléchargez l'exécutable dans le dossier `dist/`.
- Double-cliquez sur le fichier `decompresser_zips.exe` pour l'exécuter.

## Auteur
MHAJAR Youness
=======
# decompression_project



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.emse.fr/youness.mhajar/decompression_project.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.emse.fr/youness.mhajar/decompression_project/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Décompresseur Automatique

## Description
Ce projet permet de décompresser automatiquement des fichiers ZIP et RAR dans un dossier de destination spécifié.

## Instructions d'Utilisation

1. **Préparation des fichiers compressés :**
   - Téléchargez tous vos fichiers ZIP et RAR dans un même dossier.

2. **Configurer les chemins d'accès :**
   - Ouvrez le script Python et modifiez les variables suivantes pour indiquer les chemins d'accès appropriés :
     ```python
     # Chemin vers le dossier contenant les fichiers compressés
     COMPRESSED_FOLDER = 'chemin/vers/votre/dossier/source'
     
     # Chemin vers le dossier de destination
     EXTRACT_FOLDER = 'chemin/vers/votre/dossier/destination'
     ```

3. **Utilisation de l'exécutable :**
   - Téléchargez l'exécutable généré dans le dossier `dist/`.
   - Placez l'exécutable dans le même répertoire que vos fichiers compressés.
   - Double-cliquez sur le fichier `decompresser_zips.exe` pour l'exécuter.
   - Les fichiers décompressés seront automatiquement placés dans le dossier de destination spécifié.

## Remarques
- **Compatibilité des formats :**
  Ce projet prend en charge les fichiers compressés aux formats suivants :
  - `.zip`
  - `.rar`

- **Dépendances :**
  Si vous exécutez le script Python directement, assurez-vous que les bibliothèques suivantes sont installées :
  - `zipfile` (inclus avec Python)
  - `rarfile` (à installer avec `pip install rarfile`)

## Auteur
MHAJAR Youness

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
>>>>>>> origin/main
