""" gére les évenements : ce qui ce passe et leurs probabilités """
import random
def sécheresse(nb_eau:int,difficulté:int):
  """événement de sécheresse qui entraîne une perte de nb_eau"""
    if nb_eau >= 4:
        pertes= random.randint(1,nb_eau//(5-difficulté)) #Avec difficulté de 1 à 4
        nb_eau = nb_eau - pertes 
    else:# Si nb_eau < 4 alors nb_eau//4 = 0 donc ici cas spécifique 
        nb_eau = nb_eau - min(nb_eau,difficulté)   
    # A afficher : "Une période de sécheresse vous fait perdre",pertes,"unité(s) d'eau")
    return nb_eau
