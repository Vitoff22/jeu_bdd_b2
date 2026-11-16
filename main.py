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
    # tant que vrai
        #si le joueur n'a pas choisi 3 perso
            #retourner faux
        #si le perso n'existe pas dans la liste
            #retouner faux
        #sinon
            #retourner vrai

#equipe complete
    #tant que equipe n'est pas egale a 3
        #retourner faux
    #sinon
        #retourner vrai