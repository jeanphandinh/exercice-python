class Livre:
    def __init__(self, titre, auteur, disponible=True):
        self.titre = titre
        self.auteur = auteur
        self.disponible = disponible

    def emprunter(self):
        if not self.disponible:
            raise ValueError("Ce livre est déjà emprunté.")
        self.disponible = False

    def retourner(self):
        self.disponible = True

    def to_dict(self):
        return {
            "titre": self.titre,
            "auteur": self.auteur,
            "disponible": self.disponible
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["titre"],
            data["auteur"],
            data.get("disponible", True)
        )
