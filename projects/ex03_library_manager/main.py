from library import Bibliotheque


def afficher_resultats(resultats):
    if not resultats:
        print("Aucun résultat.")
        return

    print("\n=== Résultats ===")
    for livre in resultats:
        statut = "Disponible" if livre.disponible else "Emprunté"
        print(f"- {livre.titre} / {livre.auteur} [{statut}]")


def menu():
    biblio = Bibliotheque()

    while True:
        print("\n=== Bibliothèque personnelle ===")
        print("1. Ajouter un livre")
        print("2. Afficher les livres")
        print("3. Rechercher un livre")
        print("4. Emprunter un livre")
        print("5. Retourner un livre")
        print("6. Quitter")

        choix = input("Votre choix : ").strip()

        if choix == "1":
            titre = input("Titre : ").strip()
            auteur = input("Auteur : ").strip()

            if titre == "" or auteur == "":
                print("Titre ou auteur invalide.")
            else:
                biblio.ajouter_livre(titre, auteur)
                print("Livre ajouté.")
        elif choix == "2":
            biblio.afficher_livres()
        elif choix == "3":
            mot_cle = input("Recherche : ").strip()
            resultats = biblio.rechercher_livre(mot_cle)
            afficher_resultats(resultats)
        elif choix == "4":
            biblio.afficher_livres()
            try:
                index = int(input("Numéro du livre à emprunter : ")) - 1
                biblio.emprunter_livre(index)
            except ValueError:
                print("Veuillez entrer un nombre valide.")
        elif choix == "5":
            biblio.afficher_livres()
            try:
                index = int(input("Numéro du livre à retourner : ")) - 1
                biblio.retourner_livre(index)
            except ValueError:
                print("Veuillez entrer un nombre valide.")
        elif choix == "6":
            print("Au revoir.")
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    menu()
