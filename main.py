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


#fonction lancer le combat
    #initialiser le score a 0
    ##afficher manche 1
    #afficher les points de vie des perso
    #afficher les points de vie du monstre

#tant que le monstre est en vie et que l membre de l'equipe aussi
    #continue le combat
    #si le monstre meurt passe a la manche 2
    #si toute l'equipe meurt
        #afficher tu as perdu la manche
    #sinon continuer

#manche 2
    #afficher manche 2
    #tant que le monstre est en vie et que l membre de l'equipe aussi
        #continue le combat
        #si le monstre meurt passe a la manche 3
        #si toute l'equipe meurt
            #afficher tu as perdu la manche 2
        #sinon continuer

#manche 3
    #afficher manche3
    #tant que le monstre est en vie et que l membre de l'equipe aussi
        #continue le combat
        #si le monstre meurt
            #afficher bravo tu as gagné
        #si toute l'equipe meurt
            #afficher tu as perdu la manche 3
        #sinon continuer