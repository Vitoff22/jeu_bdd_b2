#afficher le menu(demarrer le jeu, option, quitter)

#récuperer le choix de l'utilisateur
    #tant que le choix n'est pas valide
        #demander au joueur de saisir un choix
        #si le choix est un nombre valide
            #afficher que le choix n'est pas valide
            #redemander un choix
        #si le choix n'est pas compris la liste du menu
            #afficher que le choix n'est pas valide
            #redemander un choix
        #sinon  
            #retourner vrai 
            #break

#demander au joueur de choisir un pseudo
    #tant que le pseudo n'est pas valide
        #entrez son pseudo
        #si  le pseudo est plus grand que le maximum ou que le minimum  
            #afficher un message d'erreur
        #else
            #retourner vrai
            #break

#faire choisir 3 personnages au joueur
    #creer une equipe vide
    #afficher la liste des perso
    # tant que l'equipe contient pas 3 joueurs
        #afficher les perso disponibles
        #demander au joueur de choisir

        #si le joueur n'existe pas
            #afficher message d'erreur
            #redemander un choix
        #si le perso est deja dans l'equipe
            #afficher un message d'erreur
            #redemander un choix
        #sinon
            #retourner vrai

#equipe complete
    #si contient 3 perso
        #afficher l'equipe complete
        #passer au combat
    #sinon
        #retourner choisir 3 perso

#combat

#prendre aleatoirement un premier monstre a affronté
#afficher les points de vie du perso
#afficher les points de vie du monstre

#tant que le monstre est en vie et que l membre de l'equipe aussi
    #