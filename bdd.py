from pymongo import MongoClient

#champs de moongodb
CHAMP_NOM = "name"
CHAMP_PV = "hp"
CHAMP_DEGATS = "atk"
CHAMP_PSEUDO = "pseudo"

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

#fonction recuperer_pseudo_db(db)
def recuperer_pseudo_db(db):
    #retourne la liste des pseudos enregistrés dans MongoDB
    return db["user"].distinct(CHAMP_PSEUDO)

# fonction enregistrer_score(db, pseudo, score, resultat)
def enregistrer_score(db, pseudo, score, resultat):
    # créer un document avec les résultats
    document = {CHAMP_PSEUDO: pseudo, "score": score, "resultat": resultat}
    # enregistrer le document dans MongoDB
    db["user"].insert_one(document)

def recuperer_meilleurs_scores(db):
    # garder seulement les doc qui ont un score numérique
    filtre = {"score": {"$type": "number"}}
    # trier du plus grand au plus petit score et garder les dix premiers
    scores = db["user"].find(filtre).sort("score", -1).limit(10)
    return list(scores)
