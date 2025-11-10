#!/usr/bin/env python3
# Script d'information systeme avec espace disque

# Import des modules
import os          #Gestion systeme/fichiers
import platform    #Infos sur la plateforme/OS
import datetime    #Gestion date/heure
import shutil      #Pour statistique disque

# Titre du script
print("=" * 70)
print("         INFORMATIONS SYSTEME + ESPACE DISQUE")
print("=" * 70)

# === SECTION DATE & HEURE ===
print(f"\n DATE & HEURE")
# strftime formatte la date selon le pattern donne
print(f"   {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

# === SECTION SYSTEME ===
print(f"\n SYSTEME")
# platform.system() retourne 'Linux', 'Windows', 'Darwin' (macOS)
print(f"   OS : {platform.system()} {platform.release()}")
# Version detaillee du systeme
print(f"   Version : {platform.version()}")
# Architecture processeur (x86_64, arm64, etc.)
print(f"   Architecture : {platform.machine()}")

# === SECTION PYTHON ===
print(f"\n PYTHON")
# Version Python installee
print(f"   Version : {platform.python_version()}")
# Type d'implementation (CPythonm PyPy, Jython, etc.)
print(f"   Implementation : {platform.python_implementation()}")

# === SECTION UTILISATEUR ===
print(f"\n UTILISATEUR")
# Nom de l'utilisateur actuel (variable d'environnement USER)
print(f"   User : {os.getenv('USER', 'Inconnu')}")
# Chemin du repertoire home de l'utilisateur
print(f"   Home : {os.path.expanduser('~')}")
# Repertoire de travail actuel
print(f"   Repertoire actuel : {os.getcwd()}")

# === SECTION ESPACE DISQUE ===
print(f"\n ESPACE DISQUE")

# Bloc try/except car disu_usage peut echouer sur certains systemes
try:
    # disk_usage retourne un tuple (total, used, free) en octets
    total, used, free = shutil.disk_usage("/")

    # Conversion octets -> Go (divise par 1024 trois fois)
    #1 go = 1024 Mo = 1024 * 1024 Ko = 1024 * 1024 * 1024 octets
    total_gb = total / (1024 ** 3)
    used_gb = used / (1024 ** 3)
    free_gb = free / (1024 ** 3)

    # Calcul du pourcentage utilise
    percent_used = (used / total) * 100

    # Affichage des valeurs
    # :.2f = format avec 2 decimales
    print(f"   Total : {total_gb:.2f} Go")
    print(f"   Utilise : {used_gb:.2f} Go ({percent_used:.1f}%)")
    print(f"   Libre : {free_gb:.2f} Go")

    # === BARRE DE PROGRESSION VISUELLE ===
    bar_length = 40  #Longueur de la barre en caracteres

    # Calcul du nombre de caracteres remplis
    # Si 75% utilise et barre de 40 chars -> 30 chars remplis
    filled = int(bar_length * percent_used / 100)

    # Construction de la barre
    # █ = caractère plein (rempli)
    # ░ = caractère vide
    bar = "█" * filled + "░" * (bar_length - filled)

    # Affichage de la barre
    print(f"\n   [{bar}] {percent_used:.1f}%")

# Si erreur lors de la recuperation des infos disque
except Exception as e:
    print(f" Impossible de recuperer les infos disque : {e}")

# === SECTION RESEAU ===
print(f"\n RESEAU")
# Nom de la machine (hostname)
print(f"   Hostname : {platform.node()}")

# Ligne de separation finale
print("\n" + "=" * 70)
 
