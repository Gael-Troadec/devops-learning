#!/usr/bin/env python3
# Shebang - indique que c'est un script Python

# Import des modules necessaires
import os        #Gestion fichiers/dossiers
import shutil    #Copie de dossiers entiers
import datetime  #Gestion dates/heures
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s -  %(message)s',
    handlers=[
        logging.FileHandler('backup.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Affichage du titre
logger.info("Starting backup script")
print("=" * 60)
print("          BACKUP AUTOMATIQUE")
print("=" * 60)

# Demande a l'utilisateur les chemins source et destination
source = input("\n Dossier a sauvegarder : ")
destination = input(" Dossier de destination des backups : ")

# Verifie que le dossier source existe
if not os.path.exists(source):
    logger.error(f"Source directory does not exist: {source}")
    exit(1) # Arrete le script avec code erreur 1

# Verifie que la source est bien un dossier (pas un fichier)
if not os.path.exists(source):
    logger.error(f"\n Error : '{source}' is not a folder")
    exit(1)

# Cree le dossier de destination s'il n'existe pas
# exist_ok=True evite l'erreur si le dossier existe deja
os.makedirs(destination, exist_ok=True)

# Genere un timestamp pour nommer le backup de facon unique
# Format : YYYYMMDD_HHMMSS (ex: 20251106_143022)
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
nom_backup = f"backup_{timestamp}"
chemin_backup = os.path.join(destination, nom_backup)

# Affiche les infos avant de commencer
logger.info("Backup path creation")
print(f"\n Creation du backup...")
print(f"  Source : {os.path.abspath(source)}")
print(f"  Destination : {chemin_backup}")

# Bloc try/except pour gerer les erreurs possibles
try:
    # Copie recursive du dossier source vers destination
    logger.info("Copy of all folders")
    shutil.copytree(source, chemin_backup)

    # Calcul de la taille totale du backup
    taille_totale = 0 #En Octets

    # Parcourt tous les fichiers du backup
    # os.walk parcourt recursivement tous les sous-dossiers
    for root, dirs, files in os.walk(chemin_backup):
        for fichier in files:
            # Construit le chemin complet du fichier
            chemin_fichier = os.path.join(root, fichier)
            # Ajoute la taille du fichier au total
            taille_totale += os.path.getsize(chemin_fichier)

    # Conversion de Octets vers Mo (divise par 1024 deux fois)
    taille_mo = taille_totale / 1024 / 1024

    # Affichage du succes avec infos
    logger.info("Backup created successfully")
    print(f"\n Backup cree avec succes !")
    print(f"Taille : {taille_mo:.2f} Mo")
    print(f"Emplacement : {chemin_backup}")

# Si une erreur se produit pendant la copie
except Exception as e:
    logger.error("Error during backup creation: {e}")
    print(f"\n Erreur lors de la creation du backup :")
    print(f"  {e}")
    exit(1)

# Ligne de separation finale
print("\n" + "=" * 60)
