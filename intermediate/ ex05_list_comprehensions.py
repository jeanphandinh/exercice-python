# Exercice 5 — List comprehensions

nombres = [1, 2, 3, 4, 5, 6]

carres = [n * n for n in nombres]
pairs = [n for n in nombres if n % 2 == 0]

print("Nombres :", nombres)
print("Carrés :", carres)
print("Pairs :", pairs)
