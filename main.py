#afficher le menu(demarrer le jeu, option, quitter)

#récuperer le choix de l'utilisateur
    #tant que le choix n'est pas valide
        #demander au joueur de saisir un choix
        #si le choix est un nombre valide
            #afficher un message d'erreur
            #redemander un choix
        #si le choix n'est pas compris la liste du menu
            #afficher que le choix n'est pas valide
            #redemander un choix
        #sinon  
            #retourner vrai 
            #break

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
    #si le joueur n'existe pas dans mongoDB
        #afficher message d'erreur
        #redemander un choix

    #si le perso est deja dans l'equipe
        #afficher un message d'erreur
        #redemander un choix

    #sinon
        #ajouteer une copie du personnage a l'equipe
        #afficher le personnage ajouté
        #afficher le nombre de perso selectionnés

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


#fonction lancer le combat(equipe)
    #initialiser le score a 0
    ##afficher manche 1
    
    #pour manche 1 a 3
        #appeler jouer manche()
        #si le monstre meurt passe a la manche 2
        #si toute l'equipe meurt
            #afficher tu as perdu la manche
        #sinon 
            #ajouter les points au score
        #retourner les resultats de la partie

#fonction combattre(equipe, monstre)
    #tant que le monstre et l'equipe sont vivants
        #appeler tour equipe()
            #appeler tour monstre()
    #appeler verifier victoire
    #retourner le resultat

#fonction tour equipe(equipe, monstre)
    #pour chaque personnage de l'equipe
        #si le monstre est mort
            #stopper le tour
        #si le perso est vivant
            #appeler attaque monstre

#fonction attaquer monstre(perso, monstre)
    # récupérer les dégâts du personnage
    # appeler calculer_degats()
    # retirer les dégâts aux PV du monstre
    # afficher les dégâts
    # afficher les PV restants

#fonction tour monstre
    # recuperer les perso vivants
    # choisir un perso vivant aleatoirement 
    # appeler attaque monstre

#fonction attaquer personnage(monstre, personnage)
    # récupérer les dégâts du monstre
    # appeler calculer_degats()
    # retirer les dégâts aux PV du personnage
    # afficher les dégâts
    # afficher les PV restants


#fonction ajouter score
    #si l'utilisateur gagne
        #afficher tu as gagné un point
        #ajouter 1 au score

    #elif si l'utilisateur perd
        #afficher tu as perdu un point
        #enlever un point

    #else
        #afficher le score n'a pas changé