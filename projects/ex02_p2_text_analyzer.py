# Projet P2 — Analyseur de texte

from collections import Counter
import string


def lire_fichier(nom_fichier):
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            return fichier.read()
    except FileNotFoundError:
        print("Erreur : fichier introuvable.")
        return None
    except OSError:
        print("Erreur : impossible de lire le fichier.")
        return None


def nettoyer_texte(texte):
    texte = texte.lower()

    for caractere in string.punctuation:
        texte = texte.replace(caractere, "")

    return texte


def compter_lignes(texte):
    return len(texte.splitlines())


def compter_mots(texte):
    mots = texte.split()
    return len(mots)


def compter_caracteres(texte):
    return len(texte)


def mots_frequents(texte, limite=5):
    mots = texte.split()
    compteur = Counter(mots)

    resultats = sorted(
        compteur.items(),
        key=lambda element: element[1],
        reverse=True
    )

    return resultats[:limite]


def analyser_fichier():
    nom_fichier = input("Nom du fichier à analyser : ").strip()

    texte = lire_fichier(nom_fichier)

    if texte is None:
        return

    texte_nettoye = nettoyer_texte(texte)

    nb_lignes = compter_lignes(texte)
    nb_mots = compter_mots(texte_nettoye)
    nb_caracteres = compter_caracteres(texte)

    print("\n=== Analyse du fichier ===")
    print("Nombre de lignes :", nb_lignes)
    print("Nombre de mots :", nb_mots)
    print("Nombre de caractères :", nb_caracteres)

    print("\n=== 5 mots les plus fréquents ===")
    for mot, frequence in mots_frequents(texte_nettoye):
        print(f"{mot} : {frequence}")


if __name__ == "__main__":
    analyser_fichier()
