# Exercice 2 — Exceptions

try:
    a = int(input("Entrez un premier nombre : "))
    b = int(input("Entrez un deuxième nombre : "))
    resultat = a / b
    print("Résultat :", resultat)
except ValueError:
    print("Erreur : veuillez entrer des nombres valides.")
except ZeroDivisionError:
    print("Erreur : division par zéro impossible.")
