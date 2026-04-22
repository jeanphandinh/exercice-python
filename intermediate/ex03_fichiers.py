# Exercice 3 — Fichiers

with open("message.txt", "w", encoding="utf-8") as fichier:
    fichier.write("Bonjour, ceci est un fichier Python.\n")
    fichier.write("J'apprends à lire et écrire dans un fichier.")

with open("message.txt", "r", encoding="utf-8") as fichier:
    contenu = fichier.read()

print(contenu)
