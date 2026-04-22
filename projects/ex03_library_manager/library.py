import json
from pathlib import Path
from models import Livre


FICHIER = Path("bibliotheque.json")


class Bibliotheque:
    def __init__(self):
        self.livres = []
        self.charger()

    def charger(self):
        if FICHIER.exists():
            try:
                with open(FICHIER, "r", encoding="utf-8") as fichier:
                    data = json.load(fichier)
                    self.livres = [Livre.from_dict(item) for item in data]
            except (json.JSONDecodeError, OSError):
                self.livres = []

    def sauvegarder(self):
        with open(FICHIER, "w", encoding="utf-8") as fichier:
            json.dump(
                [livre.to_dict() for livre in self.livres],
                fichier,
                indent=4,
                ensure_ascii=False
            )

    def ajouter_livre(self, titre, auteur):
        livre = Livre(titre, auteur)
        self.livres.append(livre)
        self.sauvegarder()

    def afficher_livres(self):
        if not self.livres:
            print("Aucun livre enregistré.")
            return

        print("\n=== Liste des livres ===")
        for index, livre in enumerate(self.livres, start=1):
            statut = "Disponible" if livre.disponible else "Emprunté"
            print(f"{index}. {livre.titre} - {livre.auteur} [{statut}]")

    def rechercher_livre(self, mot_cle):
        resultats = []

        for livre in self.livres:
            if mot_cle.lower() in livre.titre.lower() or mot_cle.lower() in livre.auteur.lower():
                resultats.append(livre)

        return resultats

    def emprunter_livre(self, index):
        try:
            self.livres[index].emprunter()
            self.sauvegarder()
            print("Livre emprunté avec succès.")
        except IndexError:
            print("Index invalide.")
        except ValueError as erreur:
            print(erreur)

    def retourner_livre(self, index):
        try:
            self.livres[index].retourner()
            self.sauvegarder()
            print("Livre retourné avec succès.")
        except IndexError:
            print("Index invalide.")
