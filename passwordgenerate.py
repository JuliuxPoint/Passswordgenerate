import random
import string

def generer_mot_de_passe(taille=12):
    # Définir les caractères possibles pour le mot de passe
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Générer un mot de passe aléatoire de la taille spécifiée
    mot_de_passe = ''.join(random.choice(caracteres) for i in range(taille))
    
    return mot_de_passe

# Exemple d'utilisation
if __name__ == "__main__":
    taille_mot_de_passe = 16  # Vous pouvez changer la taille du mot de passe ici
    mot_de_passe = generer_mot_de_passe(taille_mot_de_passe)
    print("Mot de passe généré:", mot_de_passe)
