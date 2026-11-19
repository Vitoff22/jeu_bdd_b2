from random import choice
from pymongo import MongoClient

#taille de l'equipe
TAILLE_EQUIPE = 3

#champs de moongodb
CHAMP_NOM = "name"
CHAMP_PV = "hp"
CHAMP_DEGATS = "atk"
CHAMP_PSEUDO = "pseudo"


#fonction main()
def main():
    #connecter MongoDB et recuperer db
    db = connecter_mongodb()
    #tant que vrai
    while True:
        #appeler demander_menu() et recuperer le choix
        choix = demander_menu()
        #si demarrer
        if choix == 1:
            #appeler demarrer_partie(db)
            demarrer_partie(db)
        #ou si le choix est voir les perso
        elif choix == 2:
            #appeler afficher_personnages_dispo(db)
            afficher_personnages_dispo(db)
        #sinon
        else:
            #arreter le jeu
            break


#fonction demander_menu()
def demander_menu():
    #tant que vrai
    while True:
        #afficher les options numerotés
        print("1. Démarrer")
        print("2. Voir les personnages")
        print("3. Quitter")
        # demander au joueur de saisir un choix
        try:
            choix = int(input("Ton choix : "))
        # si le choix n'est pas un entier valide
        except ValueError:
            # afficher un message d'erreur
            print("Tu dois saisir un entier.")
            continue
        # sinon si le choix n'est pas compri entre 1 et 3
        if 1 <= choix <= 3:
            return choix
            # afficher un message d'erreur
        print("Ton choix n'est pas dans les options")        



# Fonction connecter_mongodb()
def connecter_mongodb():
    # etablir la connexion à MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    # sélectionner la base de données
    # retourner db
    return client["jeu_video"]

# Fonction recuperer_personnages(db)
def recuperer_personnages(db):
    # récupérer les personnages dans MongoD
    # retourner la liste des personnages
    return list(db["characters"].find())

# Fonction recuperer_monstres(db)
def recuperer_monstres(db):
    # récupérer les monstres dans MongoDB
    # retourner la liste des monstres
    return list(db["monsters"].find())


# fonction demarrer_partie(db)
def demarrer_partie(db):
    #recuperer les perso et monstres
    personnages, monstres = charger_combattants(db)
    #appeler demander_pseudo
    pseudo = demander_pseudo(db)
    #appeler demander_equipe
    equipe = demander_equipe(personnages)
    # appeler lancer_combat(equipe, monstres) et recupere le score et le resultat
    score, resultat = lancer_combat(equipe, monstres)
    # appeler enregistrer_score(db, pseudo, score, resultat)
    enregistrer_score(db, pseudo, score, resultat)
    # afficher le resultat final et le score
    print(f"\nRésultat final : {resultat} | Score : {score}")

#fonction charger_combattants(db)
def charger_combattants(db):
    """Récupérer les listes et vérifier qu'une partie est possible."""
    #recuperer les personnages
    personnages = recuperer_personnages(db)
    #si moins de TAILLE_EQUIPE personnages, afficher une erreur
    if len(personnages) < TAILLE_EQUIPE:
        print("Il n'y a pas assez de personnages pour former une équipe.")
        return [], []
    #recuperer les monstres
    monstres = recuperer_monstres(db)
    #si aucun monstre, afficher une erreur
    if not monstres:
        print("Aucun monstre disponible.")
    #retourner les deux listes
    return personnages, monstres

#fonction demander_pseudo(db)
def demander_pseudo(db):
    #recuperer pseudos avec recuperer_pseudo_db(db)
    pseudos = recuperer_pseudo_db(db)
    #tant que Vrai
    while True:
        #entrez son pseudo et enlever les espaces au debut et a la fin
        pseudo = input("Entre ton pseudo : ").strip()
        #si est_pseudo_valide(pseudo, pseudos) est faux
        if not est_pseudo_valide(pseudo, pseudos):
            #afficher un message d'erreur
            print("Ton pseudo n'est pas valide")
        #else
        else:
            #retourner pseudo
            return pseudo

#fonction est_pseudo_valide(pseudo, pseudos)
def est_pseudo_valide(pseudo, pseudos):
    #si la longueur du pseudo est comprise en 3 et 10 et que le pseudo n'est pas dans pseudos
    if  3 <= len(pseudo) <= 10 and pseudo not in pseudos:
        #retourner vrai
        return True
    #retourner faux
    return False

#fonction recuperer_pseudo_db(db)
def recuperer_pseudo_db(db):
    #retourne la liste des pseudos enregistrés dans MongoDB
    return db["user"].distinct(CHAMP_PSEUDO)


#fonction demander_equipe(personnages)
def demander_equipe(personnages):
    #creer une equipe vide
    equipe = []
    # tant que l'equipe contient moins de TAILLE_EQUIPE personnages
    while len(equipe) < TAILLE_EQUIPE:
        #afficher les perso disponibles
        afficher_personnages(personnages)
        #demander au joueur de choisir
        numero = demander_numero_personnage(personnages)
        personnage = personnages[numero - 1]

        #si est_personnage_valide(personnage, equipe, personnages)
        if est_personnage_valide(personnage, equipe, personnages):
            #ajouter une copie du personnage à l'equipe
            equipe.append(personnage.copy())
        #sinon
        else:
            #afficher un message d'erreur
            print("Ton personnage est deja dans l'equipe")

    #retourner l'equipe complete
    return equipe

#fonction demander_numero_personnage(personnages)
def demander_numero_personnage(personnages):
    #tant que vrai
    while True:
        #demander un numero et essayer de le convertir en entier
        try:
            numero = int(input("Choisis un personnage : "))
        except ValueError:
            print("Tu dois saisir un entier.")
            continue
        #si le numero est dans la liste, le retourner
        if 1 <= numero <= len(personnages):
            return numero
        #sinon afficher un message d'erreur
        print("Ce numéro n'est pas dans la liste.")

#fonction est_personnage_valide(personnage, equipe, personnages)
def est_personnage_valide(personnage, equipe, personnages):
    # si le personnage n'existe pas dans la liste
    if personnage not in personnages:
        # retourner faux
        return False
    # si le personnage est déjà dans l'équipe
    if personnage in equipe:
        # retourner faux
        return False
    # retourner vrai
    return True


# fonction lancer_combat(equipe, monstres)
def lancer_combat(equipe, monstres):
    # initialiser le score à 0
    score = 0
    # pour chaque manche de 1 à 3
    for manche in range(1,4):
        #recuperer le resultat du combat de jouer_manche(equipe, monstres, manche)
        resultat = jouer_manche(equipe, monstres, manche)
        # remplacer score par le resultat de calculer_score(score, resultat)
        score = calculer_score(score, resultat)
        # si le résultat est une defaite
        if resultat == "defaite":
            #arreter les manches
            break
    # retourner le score et le résultat final
    return score, resultat


# fonction combattre(equipe, monstre)
def combattre(equipe, monstre):
    # tant que est_vivant(monstre) et est_equipe_vivante(equipe)
    while est_vivant(monstre) and est_equipe_vivante(equipe):
        # appeler tour_equipe(equipe, monstre)
        tour_equipe(equipe, monstre)
        # si le monstre est encore vivant
        if est_vivant(monstre):
           # appeler tour_monstre(equipe, monstre)
           tour_monstre(equipe, monstre)
    # appeler verifier_victoire(monstre)
    # retourner le résultat
    return verifier_victoire(monstre)


#fonction tour_equipe(equipe, monstre)
def tour_equipe(equipe, monstre):
    #pour chaque personnage de l'equipe
    for personnage in equipe:
        #si le monstre est mort
        if not est_vivant(monstre):
            #stopper le tour
            break
        #si le perso est vivant
        if est_vivant(personnage):
            #appeler attaquer(perso, monstre)
            attaquer(personnage, monstre)
    ...


#fonction attaquer(attaquant, cible)
def attaquer(attaquant, cible):
    # récupérer les dégats de l'attaquant
    degats = attaquant[CHAMP_DEGATS]
    # retirer les degats aux PV de la cible
    cible[CHAMP_PV] = max(0, cible[CHAMP_PV] - degats)
    # afficher les degats
    print(f"{attaquant[CHAMP_NOM]} inflige {degats} dégâts à {cible[CHAMP_NOM]}.")
    # afficher les PV restants
    print(f"PV restants : {cible[CHAMP_PV]}")

#fonction tour_monstre(equipe, monstre)
def tour_monstre(equipe, monstre):
    # recuperer les perso vivants
    personnages_vivants = [perso for perso in equipe if est_vivant(perso)]
    # choisir un perso vivant aleatoirement 
    perso = choice(personnages_vivants)
    # appeler attaquer(monstre, perso)
    attaquer(monstre, perso)


#fonction jouer_manche(equipe, monstres, manche)
def jouer_manche(equipe, monstres, manche):
    #recuperer un monstre avec tirer_monstre(monstres)
    monstre = tirer_monstre(monstres)
    #afficher le numero de manche
    print(f"\n Manche {manche}")
    # afficher les PV des personnages
    afficher_personnages(equipe)
    # afficher les PV du monstre
    print(f"Monstre : {monstre[CHAMP_NOM]} | {monstre[CHAMP_PV]} PV")
    # appeler combattre(equipe, monstre)
    # retourner le résultat
    return combattre(equipe, monstre)

# fonction est_vivant(personnage)
def est_vivant(personnage):
    return personnage[CHAMP_PV] > 0


# fonction est_equipe_vivante(equipe)
def est_equipe_vivante(equipe):
    # pour chaque personnage de l'équipe
    for personnage in equipe:
        # si est_vivant(personnage)
        if est_vivant(personnage):
            # retourner vrai
            return True
    # retourner faux
    return False


# fonction verifier_victoire(monstre)
def verifier_victoire(monstre): 
    # si les PV du monstre sont inférieurs ou égaux à 0
    if not est_vivant(monstre):
        # retourner victoire
        return "victoire"
    # retourner défaite
    return "defaite"

# fonction tirer_monstre(monstres)
def tirer_monstre(monstres):
    # sélectionner aléatoirement un monstre
    monstre = choice(monstres)
    # créer une copie du monstre
    # retourner la copie du monstre
    return monstre.copy()

# fonction enregistrer_score(db, pseudo, score, resultat)
def enregistrer_score(db, pseudo, score, resultat):
    # créer un document avec les résultats
    document = {CHAMP_PSEUDO: pseudo, "score": score, "resultat": resultat}
    # enregistrer le document dans MongoDB
    db["user"].insert_one(document)

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
        #afficher ses caracteristiques
        print(f"{numero}. {nom} | {pv} PV | {degats} dégâts")


# fonction calculer_score(score, resultat)
def calculer_score(score, resultat):
    #si resultat est une victoire
    if resultat == "victoire":
        #retourner score +1
        return score + 1
    #retourner le maximum entre 0 et score -1
    return max(0, score - 1)

if __name__ == "__main__":
    main()