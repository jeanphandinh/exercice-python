# Exercice 10 — Exceptions simples

try:
    nombre = int(input("Entrez un nombre : "))
    print("Vous avez écrit :", nombre)
except ValueError:
    print("Erreur : vous devez entrer un nombre entier.")
