# Projet P1 — Gestionnaire de notes

def ajouter_eleve(eleves):
    nom = input("Nom de l'élève : ").strip()

    if nom == "":
        print("Nom invalide.")
        return

    if nom in eleves:
        print("Cet élève existe déjà.")
    else:
        eleves[nom] = []
        print(f"{nom} a été ajouté.")


def ajouter_note(eleves):
    nom = input("Nom de l'élève : ").strip()

    if nom not in eleves:
        print("Élève introuvable.")
        return

    note_str = input("Note à ajouter : ").strip()

    try:
        note = float(note_str)
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return

    if note < 0 or note > 20:
        print("La note doit être comprise entre 0 et 20.")
        return

    eleves[nom].append(note)
    print(f"Note {note} ajoutée à {nom}.")


def calculer_moyenne(notes):
    if len(notes) == 0:
        return 0
    return sum(notes) / len(notes)


def afficher_eleves(eleves):
    if len(eleves) == 0:
        print("Aucun élève enregistré.")
        return

    print("\n=== Liste des élèves ===")
    for nom, notes in eleves.items():
        moyenne = calculer_moyenne(notes)
        print(f"{nom} | Notes : {notes} | Moyenne : {moyenne:.2f}")


def afficher_admis(eleves):
    if len(eleves) == 0:
        print("Aucun élève enregistré.")
        return

    print("\n=== Élèves ayant la moyenne ===")
    admis_trouves = False

    for nom, notes in eleves.items():
        moyenne = calculer_moyenne(notes)
        if moyenne >= 10:
            print(f"{nom} avec {moyenne:.2f}/20")
            admis_trouves = True

    if not admis_trouves:
        print("Aucun élève n'a la moyenne.")


def afficher_moyenne_eleve(eleves):
    nom = input("Nom de l'élève : ").strip()

    if nom not in eleves:
        print("Élève introuvable.")
        return

    moyenne = calculer_moyenne(eleves[nom])
    print(f"Moyenne de {nom} : {moyenne:.2f}/20")


def menu():
    eleves = {
        "Jean": [14, 12, 16],
        "Alex": [10, 9, 13]
    }

    while True:
        print("\n=== Gestionnaire de notes ===")
        print("1. Ajouter un élève")
        print("2. Ajouter une note")
        print("3. Afficher tous les élèves")
        print("4. Afficher la moyenne d'un élève")
        print("5. Afficher les élèves ayant la moyenne")
        print("6. Quitter")

        choix = input("Votre choix : ").strip()

        if choix == "1":
            ajouter_eleve(eleves)
        elif choix == "2":
            ajouter_note(eleves)
        elif choix == "3":
            afficher_eleves(eleves)
        elif choix == "4":
            afficher_moyenne_eleve(eleves)
        elif choix == "5":
            afficher_admis(eleves)
        elif choix == "6":
            print("Au revoir.")
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    menu()
