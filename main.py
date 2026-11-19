from bdd import (
    connecter_mongodb,
    enregistrer_score,
    recuperer_monstres,
    recuperer_personnages,
    )
from combat import lancer_combat
from interface import (
    afficher_meilleurs_scores,
    afficher_personnages,
    afficher_personnages_dispo,
    demander_choix,
    demander_menu,
    demander_pseudo,
)

#taille de l'equipe
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
        elif choix == 3:
            #montrer les scores
            afficher_meilleurs_scores(db)
        else:
            #arreter le jeu
            break

# fonction demarrer_partie(db)
def demarrer_partie(db):
    #recuperer les perso et monstres
    personnages, monstres = charger_combattants(db)
    # si aucun perso ou monstre est dispo ne pas lancer la game
    if not personnages or not monstres:
        return
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

#verifie que l'equipe est complete
def est_equipe_complete(equipe):
    return len(equipe) >= TAILLE_EQUIPE

#fonction demander_equipe(personnages)
def demander_equipe(personnages):
    #creer une equipe vide
    equipe = []
    disponibles = personnages.copy()
    # tant que l'equipe contient moins de TAILLE_EQUIPE personnages
    while not est_equipe_complete(equipe):
        #afficher les personnages disponibles
        afficher_personnages(disponibles)
        # choisir un numero parmi les personnages qui sont encore disponibles
        numero = demander_choix("Choisis un personnage : ", len(disponibles))
        # retirer le perso choisi et ajouter sa copie à l'équipe
        personnage = disponibles.pop(numero - 1)
        equipe.append(personnage.copy())
    #retourner l'équipe complète
    return equipe

if __name__ == "__main__":
    main()