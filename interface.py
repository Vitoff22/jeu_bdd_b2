from bdd import (
    CHAMP_DEGATS,
    CHAMP_NOM,
    CHAMP_PSEUDO,
    CHAMP_PV,
    recuperer_meilleurs_scores,
    recuperer_personnages,
    recuperer_pseudo_db,
)

#affiche les options du menu
def afficher_options_menu():
    print("\n1. Démarrer")
    print("2. Voir les personnages")
    print("3. Voir les scores")
    print("4. Quitter")

def demander_choix(message, maximum):
    # tant que le choix est invalide, redemander
    while True:
        saisie = input(message).strip()
        # verifier la saisie avant de la convertir
        if not est_saisie_numerique(saisie):
            print("Tu dois saisir un numéro.")
            continue
        choix = int(saisie)
        # retourner le choix s'il correspond a une option
        if 1 <= choix <= maximum:
            return choix
        print(f"Choisis un numéro entre 1 et {maximum}.")

#permet de demander le choix a l'utilisateur
def demander_menu():
    afficher_options_menu()
    return demander_choix("Ton choix : ", 4)

#verifie que l'utilisateur entre bien un chiffre
def est_saisie_numerique(saisie):
    return saisie.isascii() and saisie.isdigit()

#fonction demander_pseudo(db)
def demander_pseudo(db):
    #recuperer pseudos avec recuperer_pseudo_db(db)
    pseudos = recuperer_pseudo_db(db)
    #tant que Vrai
    while True:
        #entrez son pseudo et enlever les espaces au debut et a la fin
        pseudo = input("Entre ton pseudo : ").strip()
        # verifier la longueur
        if not 3 <= len(pseudo) <= 10:
         print("Ton pseudo doit contenir entre 3 et 10 caractères.")
        #previent d'un pseudo deja utilisé
        elif not est_pseudo_valide(pseudo, pseudos):
            print("Ce pseudo est déjà utilisé. Choisis-en un")
        else:
            #retourner pseudo
            return pseudo

#fonction est_pseudo_valide(pseudo, pseudos)
def est_pseudo_valide(pseudo, pseudos):
    #si la longueur du pseudo est comprise en 3 et 10 et que le pseudo n'est pas présent dans la db
    if  3 <= len(pseudo) <= 10 and pseudo not in pseudos:
        #retourner vrai
        return True
    #retourner faux
    return False

# fonction afficher_personnages_dispo(db)
def afficher_personnages_dispo(db):
    #appeler recuperer_personnages(db)
    personnages = recuperer_personnages(db)
    #appeler afficher_personnages(personnages)
    afficher_personnages(personnages)

# fonction afficher_personnages(personnages)
def afficher_personnages(personnages):
    # pour chaque personnage en tant que perso
    for numero, perso in enumerate(personnages, start=1):
        # afficher le nom et les caractéristiques du perso
        nom = perso[CHAMP_NOM]
        pv = perso[CHAMP_PV]
        degats = perso[CHAMP_DEGATS]
        #afficher ses caractéristiques
        print(f"{numero}. {nom} | {pv} PV | {degats} dégâts")

def afficher_meilleurs_scores(db):
    # recuperer les scores et verifier que la liste n'est pas vide
    scores = recuperer_meilleurs_scores(db)
    if not scores:
        print("Aucun score enregistré.")
        return
    # afficher les scores avec leur rang
    print("\nMeilleurs scores")
    for rang, document in enumerate(scores, start=1):
        pseudo = document.get(CHAMP_PSEUDO, "Inconnu")
        print(f"{rang}. {pseudo} | Score : {document['score']}")
