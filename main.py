#fonction main()
    #connecter MongoDB et recuperer db
    #tant que vrai
        #appeler demander_menu() et recuperer le choix
        #si demarrer
            #appeler demarrer_partie(db)
        #ou si le choix est voir les perso
            #appeler afficher_personnages_disponibles(db)
        #sinon
            #arreter le jeu


#fonction demander_menu()
    #tant que vrai
        #afficher les options numerotés
        # demander au joueur de saisir un choix
        # si le choix n'est pas un nombre valide
            # afficher un message d'erreur
        # sinon si le choix n'est pas compri entre 1 et 3
            # afficher un message d'erreur
        # sinon
            # retourner le choix converti en entier



# Fonction connecter_mongodb()
    # etablir la connexion à MongoDB
    # sélectionner la base de données
    # retourner db

# Fonction récupérer les personnages
    # récupérer les personnages dans MongoDB
    # retourner la liste des personnages

# Fonction récupérer les monstres
    # récupérer les monstres dans MongoDB
    # retourner la liste des monstres



# fonction demarrer_partie(db)
    # appeler choisir_pseudo()
    # appeler creer_equipe(personnages)
    # appeler lancer_combat(equipe, monstres)
    # recupere le score et le resultat
    # appeler enregistrer_score()
    # afficher le resultat final



#fonction demander_pseudo(db)
    #tant que Vrai
        #entrez son pseudo
        #appeler la fonction pseudo_valide

        #si le pseudo  est faux (appeler la fonction verifier le pseudo)
            #afficher un message d'erreur

        #else
            #retourner pseudo

#fonction pseudo_valide
    #si la longueur du pseudo est comprise en 3 et 10 et que le pseudo n'est pas dans liste pseudo de mongoDB
        #retourner vrai
    #retourner faux

#fonction recuperer_pseudo_db
    #retourne liste pseudo


#fonction demander_equipe(personnages)
    #creer une equipe vide
    #afficher la liste des perso

    # tant que l'equipe n'est pas complete
        #afficher les perso disponibles
        #demander au joueur de choisir

        #appeler la fonctin verifier personnage

    #retourner l'equipe complete


#fonction personnage_valide(personnage, equipe, personnages)
    # si le personnage n'existe pas dans la liste
        # retourner faux
    # si le personnage est déjà dans l'équipe
        # retourner faux
    # retourner vrai


#fonction afficher l'equipe
    #afficher les membres de l'equipe


# fonction lancer_combat(equipe, monstres)
    # initialiser le score à 0
    # pour chaque manche de 1 à 3
        #recuperer le resultat du combat de jouer_manche()
        # appeler calculer_score(score, resultat)
        # si le résultat est une defaite
            #arreter les manches
    # si les 3 manches sont gagnées
        #afficher le victoire finale 
    # retourner le score et le résultat final


# fonction combattre(equipe, monstre)
    # tant que le monstre et l'équipe sont vivants
        # appeler tour_equipe()
        # si le monstre est encore vivant
            # appeler tour_monstre()
    # appeler verifier_victoire()
    # retourner le résultat


#fonction tour equipe(equipe, monstre)
    #pour chaque personnage de l'equipe
        #si le monstre est mort
            #stopper le tour
        #si le perso est vivant
            #appeler attaque monstre


#fonction attaquer monstre(perso, monstre)
    # récupérer les dégats du personnage
    # appeler calculer_degats()
    # retirer les degats aux PV du monstre
    # afficher les degats
    # afficher les PV restants

#fonction tour monstre
    # recuperer les perso vivants
    # choisir un perso vivant aleatoirement 
    # appeler attaque personnage

#fonction attaquer personnage(monstre, personnage)
    # recuperer les dégâts du monstre
    # appeler calculer_degats()
    # retirer les dégâts aux PV du personnage
    # afficher les degats
    # afficher les PV restants

#fonction jouer manche(equipe, monstres, manche)
    #choisir un monstre
    #afficher le numero de manche
    # afficher les PV des personnages
    # afficher les PV du monstre
    # appeler combattre()
    # retourner le résultat

# fonction est_vivant(personnage)
    # si les PV sont supérieurs à zéro
        # retourner vrai
    # sinon
        # retourner faux


# fonction equipe_vivante(equipe)
    # pour chaque personnage de l'équipe
        # si le personnage est vivant
            # retourner vrai
    # retourner faux


# fonction calculer_degats(attaquant)
    # récupérer les dégâts de l'attaquant
    # retourner les dégâts


# fonction verifier_victoire(monstre)
    # si les PV du monstre sont inférieurs ou égaux à 0
        # retourner victoire
    # sinon
        # retourner défaite


# fonction tirer_monstre(monstres)
    # sélectionner aléatoirement un monstre
    # créer une copie du monstre
    # retourner le monstre

# fonction enregistrer_score(db, pseudo, score, resultat)
    # créer un document avec les résultats
    # enregistrer le document dans MongoDB

# fonction afficher_personnages_dispo(db)
    #appeler recuperer_personnages(db)
    #récuperer personnages
    #appeler afficher_personnages(personnages)

# fonction afficher_personnages(personnages)
    # pour chaque personnage en tant que perso
        # afficher le nom et les caractéristiques du perso


# fonction calculer_score(score, resultat)
    #si resultat est une victoire
        #retourner score +1
    #retourner le maximum entre 0 et score -1

#fonction afficher_score(score)
    #afficher le score actuel