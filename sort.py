# Importation des modules
import shutil
import os
import mimetypes
import datetime

def trier():
    # Déclaration des variables
    script_name = os.path.basename(__file__)
    dir = os.listdir()
    files = []
    types = ["Images", "Documents", "Textes"]
        
    # Création des répertoires
    for i in types:
        os.makedirs(i, exist_ok=True)
    
    # Enumération des fichiers
    for f in dir:
        if os.path.isfile(f) and f != script_name:
            files.append(f)
    
    # Trie
    for f in files:
        ext, _ = mimetypes.guess_type(f)

        if ext.startswith("text"):
            shutil.move(f, "Textes")
        elif ext.startswith("application"):
            shutil.move(f, "Documents")
        elif ext.startswith("image"):
            shutil.move(f, "Images")
    
    # Vérification des répertoires
    for i in types:
        if os.path.exists(i) and len(os.listdir(i)) == 0:
            os.rmdir(i)

# Renommer les photos en .jpg
def renommer():
    dir = os.listdir("Images")
    compteur = 1

    # Renomme la photo
    for f in dir:
        if os.path.isfile(os.path.join("Images",f)) and f.lower().endswith(".jpg"):
            annee = datetime.date.today().year
            os.rename(os.path.join("Images",f), os.path.join("Images",f"vacances_{annee}_{compteur:03d}.jpg"))
            compteur += 1


# Lance le programme
if "__main__" == __name__:
    trier()

    if os.path.exists("Images"):
        renommer()