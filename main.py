from pymongo import MongoClient

TAILLE_EQUIPE = 3

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
    # recuperer personnages avec recuperer_personnages(db)
    # si moins de TAILLE_EQUIPE personnages, afficher une erreur et revenir au menu
    # recuperer pseudo avec demander_pseudo(db)
    # recuperer equipe avec demander_equipe(personnages)
    # recuperer monstres avec recuperer_monstres(db)
    # si aucun monstre, afficher une erreur et revenir au menu
    # appeler lancer_combat(equipe, monstres)
    # recupere le score et le resultat
    # appeler enregistrer_score(db, pseudo, score, resultat)
    # afficher le resultat final et le score
    ...


#fonction demander_pseudo(db)
    #recuperer pseudos avec recuperer_pseudo_db(db)
    #tant que Vrai
        #entrez son pseudo et enlever les espaces au debut et a la fin
        #si est_pseudo_valide(pseudo, pseudos) est faux
            #afficher un message d'erreur

        #else
            #retourner pseudo

#fonction est_pseudo_valide(pseudo, pseudos)
    #si la longueur du pseudo est comprise en 3 et 10 et que le pseudo n'est pas dans pseudos
        #retourner vrai
    #retourner faux

#fonction recuperer_pseudo_db(db)
    #retourne la liste des pseudos enregistrés dans MongoDB


#fonction demander_equipe(personnages)
    #creer une equipe vide

    # tant que l'equipe contient moins de TAILLE_EQUIPE personnages
        #afficher les perso disponibles
        #demander au joueur de choisir

        #si est_personnage_valide(personnage, equipe, personnages)
            #ajouter une copie du personnage à l'equipe
        #sinon
            #afficher un message d'erreur

    #retourner l'equipe complete


#fonction est_personnage_valide(personnage, equipe, personnages)
    # si le personnage n'existe pas dans la liste
        # retourner faux
    # si le personnage est déjà dans l'équipe
        # retourner faux
    # retourner vrai


# fonction lancer_combat(equipe, monstres)
    # initialiser le score à 0
    # pour chaque manche de 1 à 3
        #recuperer le resultat du combat de jouer_manche(equipe, monstres, manche)
        # remplacer score par le resultat de calculer_score(score, resultat)
        # si le résultat est une defaite
            #arreter les manches
    # retourner le score et le résultat final


# fonction combattre(equipe, monstre)
    # tant que est_vivant(monstre) et est_equipe_vivante(equipe)
        # appeler tour_equipe(equipe, monstre)
        # si le monstre est encore vivant
            # appeler tour_monstre(equipe, monstre)
    # appeler verifier_victoire(monstre)
    # retourner le résultat


#fonction tour_equipe(equipe, monstre)
    #pour chaque personnage de l'equipe
        #si le monstre est mort
            #stopper le tour
        #si le perso est vivant
            #appeler attaquer(perso, monstre)


#fonction attaquer(attaquant, cible)
    # récupérer les dégats de l'attaquant
    # retirer les degats aux PV de la cible
    # afficher les degats
    # afficher les PV restants

#fonction tour_monstre(equipe, monstre)
    # recuperer les perso vivants
    # choisir un perso vivant aleatoirement 
    # appeler attaquer(monstre, perso)

#fonction jouer_manche(equipe, monstres, manche)
    #recuperer un monstre avec tirer_monstre(monstres)
    #afficher le numero de manche
    # afficher les PV des personnages
    # afficher les PV du monstre
    # appeler combattre(equipe, monstre)
    # retourner le résultat

# fonction est_vivant(personnage)
    # si les PV sont supérieurs à zéro
        # retourner vrai
    # sinon
        # retourner faux


# fonction est_equipe_vivante(equipe)
    # pour chaque personnage de l'équipe
        # si est_vivant(personnage)
            # retourner vrai
    # retourner faux


# fonction verifier_victoire(monstre)
    # si les PV du monstre sont inférieurs ou égaux à 0
        # retourner victoire
    # sinon
        # retourner défaite


# fonction tirer_monstre(monstres)
    # sélectionner aléatoirement un monstre
    # créer une copie du monstre
    # retourner la copie du monstre

# fonction enregistrer_score(db, pseudo, score, resultat)
    # créer un document avec les résultats
    # enregistrer le document dans MongoDB

# fonction afficher_personnages_dispo(db)
def afficher_personnages_dispo(db):
    #appeler recuperer_personnages(db)
    #récuperer personnages
    #appeler afficher_personnages(personnages)
    ...

# fonction afficher_personnages(personnages)
    # pour chaque personnage en tant que perso
        # afficher le nom et les caractéristiques du perso


# fonction calculer_score(score, resultat)
    #si resultat est une victoire
        #retourner score +1
    #retourner le maximum entre 0 et score -1

if __name__ == "__main__":
    main()