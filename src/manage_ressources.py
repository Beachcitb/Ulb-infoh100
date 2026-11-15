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
    x,y = case
    if Map[x][y] == "#":
        return True
    return False

a = int(input("diff:"))
print(manage_or(0,a,0))#test de la fonction
