#fonction main()
    #connecter MongoDB
    # recuperer les personnages et les monstres
    #tant que le joueur ne quitte pas
        #afficher le menu
        #recuperer le choix
        #si demarrer
            #demarrer_partie(personnage, monstres, db)
        #sinon
            #arreter le jeu

# Fonction connecter_mongodb()
# Fonction récupérer les personnages
# Fonction récupérer les monstres

# fonction demarrer_partie(personnages, monstres, db)
    # appeler choisir_pseudo()
    # recuperer le pseudo
    # appeler creer_equipe(personnages)
    # recuperer l'equipe complete
    # appeler lancer_combat(equipe, monstres)
    # recupere le score et le resultat
    # appeler enregistrer_score()
    # afficher le resultat final

#fonction récuperer le choix de l'utilisateur
    #tant que le choix n'est pas valide
        #demander au joueur de saisir un choix
        #si le choix est un nombre n'est pas valide
            #afficher un message d'erreur
            #redemander un choix
        #si le choix n'est pas compris la liste du menu
            #afficher que le choix n'est pas valide
            #redemander un choix
        #sinon  
            #retourner le choix

#fonction choisir un pseudo
    #tant que le pseudo n'est pas valide
        #entrez son pseudo
        #appeler la fonction verifier le pseudo

        #si le pseudo  est faux
            #afficher un message d'erreur
            #redemander un pseudo
        #else
            #retourner pseudo

#fonction verifier le pseudo
    #si la longueur du pseudo est inferieur a 3 ou superieur a 10
        #retourner faux
    #sinon
        #retourner vrai

#faire choisir 3 personnages au joueur
    #creer une equipe vide
    #afficher la liste des perso

    # tant que l'equipe contient pas 3 joueurs
        #afficher les perso disponibles
        #demander au joueur de choisir

        #appeler la fonctoin verifier personnage


    #retourner l'equipe complete

#fonction verifier perso(personnage, equipe, personnages)
    # si le personnage n'existe pas dans la liste
        # retourner faux
    # si le personnage est déjà dans l'équipe
        # retourner faux
    # sinon
        # retourner vrai

#fonction verifier equipe complete
    #si contient 3 perso
        #afficher l'equipe complete
        #passer au combat
    #sinon
        #retourner choisir 3 perso

#fonction afficher l'equipe
    #si l'equipe contient 3 personnages
        #afficher l'equipe complete

    #sinon
        #afficher que l'equipe est incomplete
        #retouner au choix des perso


# fonction lancer_combat(equipe, monstres)
    # initialiser le score à 0
    # pour chaque manche de 1 à 3
        #recuperer le resultat du combat de jouer_manche()
        # appeler modifier_score(score, resultat)
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

# fonction modifier_score(score, resultat)
    # si le joueur gagne
        # ajouter 1 au score
        # afficher le point gagné
    # sinon si le joueur perd
        # retirer 1 au score sans descendre sous 0
        # afficher le point perdu
    # retourner le score