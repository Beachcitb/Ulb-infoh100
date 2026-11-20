"""gérer les differentes ressources , mais pas la population"""
import random
def manage_or(nb_or:int,difficulté:int,tour:int,seed:int=None):
    random.seed(seed)
    """or intial depend de la difficulté choisi et nb_or est le nombre d'or par tour"""
    if tour== 0:#initialise la quantité d'or (dépend de la difficulté 1 facile 4 dur)
        nb_or = random.randint(0,10)//difficulté
    #si achat d'objet , de construction ou minage d'or il faut que le nombre d'or soit mis a jour
    return nb_or
def is_or(case:tuple,Map:list):
    """regarde si une case possède de l'or"""
    x,y = case
    if Map[x][y] == "#":
        return True
    return False

a = int(input("diff:"))
print(manage_or(0,a,0))#test de la fonction



def manage_eau(nb_eau:int,difficulté:int,tour:int,nb_champ:int,nb_puits:int,seed:int=None):
    """
    Gère la quantité d'eau au cours des tours : 
    Selon ma vision chaque tour, "une eau" sera consommer par nb de champ sur la map.
    Si quantité d'eau insuffisante pour alimenter tout les champs, le nb_eau reste identique et les champs n'avance pas de 1 tour dans leurs production (Reste à faire)
    Lorsque construit, le batiment de puits permet d'augementer nb_eau de 1 chaque tour
    L'événement de sécheresse réduit le nb d'eau et celui de pluie l'augmente selon les reservoirs d'eau (batiment) construits (Voir partie events)   
    A revoir si idée différente et peut-être à preciser ce fontionnement dans l'intro du jeu pour le joueur
    """
    random.seed(seed)
    if tour==0:#initialisation de la quantité d'eau
        nb_eau = random.randint(10,20)//difficulté #Commence par un nb élevé mais est à revoir selon le nb de champ que l'on voudrait que le joueur ait et nb de tours totales
    else:
        nb_eau = nb_eau - nb_champ + nb_puits
    return nb_eau
