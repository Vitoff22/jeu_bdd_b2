from random import choice
from time import sleep

from bdd import CHAMP_DEGATS, CHAMP_NOM, CHAMP_PV
from interface import afficher_personnages

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
    print(f"PV restants : {cible[CHAMP_PV]}")
    sleep(0.8)

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

# fonction calculer_score(score, resultat)
def calculer_score(score, resultat):
    #si resultat est une victoire
    if resultat == "victoire":
        #retourner score +1
        return score + 1
    #retourner le maximum entre 0 et score -1
    return max(0, score - 1)
