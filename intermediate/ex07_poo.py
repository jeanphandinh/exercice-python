# Exercice 7 — Programmation orientée objet

class Joueur:
    def __init__(self, nom, niveau):
        self.nom = nom
        self.niveau = niveau

    def afficher_infos(self):
        print("Nom :", self.nom)
        print("Niveau :", self.niveau)

    def monter_niveau(self):
        self.niveau += 1
        print(self.nom, "passe au niveau", self.niveau)


joueur1 = Joueur("Jean", 1)

joueur1.afficher_infos()
joueur1.monter_niveau()
joueur1.afficher_infos()
