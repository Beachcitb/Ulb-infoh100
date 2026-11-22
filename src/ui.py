"""gére l'interface utilisateurs, les différents choix qu'il peut faire """


def ask_difficulty():
    """demande la difficulté au joueur et verifie quel est valide"""
    difficulty = 0
    try :
        difficulty = int(input("choisi la difficulté (de 1 à 4 avec 1 facile et 4 difficile) : "))
    except : 
        print("valeur invalide")
    while not(isinstance(difficulty,int)) or difficulty < 1 or difficulty > 4:
        try :
            difficulty = int(input("entrer une valeur valide :"))
        except :
            print("valeur invalide")

    return difficulty
def ask_seed():
    """very simple function to ask the seed"""
    seed = input("enter a seed , it can be any value (integer, float, str, bytes or bytearray) :")
    return seed

def afficher_stat(nb_or,difficulty,seed,nb_eau,nb_energie,nb_engrais,nb_robot):
    """affiche les informations """
    info_gen = "Game avec difficulté : {difficulty} et seed : {seed}"
    txt = "tu as pour ce tour: {nb_or} gold ,{nb_eau} d'unité d'eau,{nb_energie} d'énergie,{nb_engrais} unité d'engrais,{nb_robot} de robot qui travail pour toi"
    print(info_gen.format(difficulty=difficulty,seed=seed))
    print(txt.format(nb_or=nb_or,nb_eau=nb_eau,nb_energie=nb_energie,nb_engrais=nb_engrais,nb_robot=nb_robot))

def afficher_action():
    """afficher les choix et construction possible , viendra plus tard"""
    pass
