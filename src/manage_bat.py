""" gére les batiments , leurs niveaux , consomation , production"""
nb_puits=0
nb_réservoir_eau=0

def puits(nb_or:int,nb_puits:int):
    """fonction qui modifie les variables lié à la construction d'un puits, affichage qui reste à faire"""
    if nb_or >= 1:
        nb_puits=nb_puits+1
        nb_or=nb_or-1
        return nb_or,nb_puits
    else:
        return "Vous n'avez pas assez de pièce d'or pour effectuer cette action"
    
def réservoir_eau(nb_or:int,nb_réservoir_eau):
    """fonction qui modifie les variables lié à la construction d'un reservoir d'eau, affichage qui reste à faire"""
    if nb_or >=2:
        nb_réservoir_eau = nb_réservoir_eau + 1
        nb_or=nb_or-2
        return nb_or, nb_réservoir_eau
    else:
        return "Vous n'avez pas assez de pièce d'or pour effectuer cette action"
