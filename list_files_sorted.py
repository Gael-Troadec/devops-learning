 #!/usr/bin/env python 3
import os

print("=" * 60)
print("     LISTEUR DE FICHIERS - TRI PAR TAILLE")
print("=" * 60)

# Demande le dossier a analyser
chemin = input("\nDossier a analyser (. pour actuel) : ")

# Verifie que le dossier existe
if not os.path.exists(chemin):
    print(f"Erreur : '{chemin}' n'existe pas")
    exit(1)

if not os.path.isdir(chemin):
    print(f"Erreur : '{chemin}' n'est pas un dossier")
    exit(1)

# Liste tous les fichiers avec leurs tailles
fichiers = []
for element in os.listdir(chemin):
    chemin_complet = os.path.join(chemin, element)

            # On ne garde que les fichiers (pas les dossiers)
if os.path.isfile(chemin_complet):
    taille = os.path.getsize(chemin_complet)
    fichiers.append((element, taille))

# Tri par taille decroissante (du plus gros au plus petit)
fichiers.sort(key=lambda x: x[1], reverse=True)

# Affichage
print(f"\n Dossier analyse : {os.path.abspath(chemin)}")
print(f"Nombre de fichiers : {len(fichiers)}\n")

if len(fichiers) == 0:
    print("Aucun fichier trouve")
else:
    print(f"{'FICHIER':<40} {'TAILLE':>15}")
    print("-" * 60)

for nom, taille in fichiers:
          # Conversion taille en Ko/Mo si necessaire
    if taille < 1024:
        taille_str = f"{taille} 0"
    elif taille < 1024 * 1024:
        taille_str = f"{taille/1024:.2f} Ko"
    else:
        taille_str = f"{taille/1024/1024:.2f} Mo"

    print(f"{nom:<37} {taille_str:>15}")

print("\n" + "=" * 60)
