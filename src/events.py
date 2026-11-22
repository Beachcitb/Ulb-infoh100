""" gére les évenements : ce qui ce passe et leurs probabilités """
import random

def sécheresse(nb_eau:int,difficulté:int):
    """fonction qui détérmine les pertes du à la sécheresse selon la difficulté"""
    if nb_eau >= 4:
        pertes= random.randint(1,(nb_eau//2)//(5-difficulté)) #Avec difficulté de 1 à 4
        nb_eau = nb_eau - pertes 
    else:# Si nb_eau < 4 alors nb_eau//4 = 0 donc ici cas spécifique 
        nb_eau = nb_eau - min(nb_eau,difficulté)        
    print("Une période de sécheresse vous fait perdre",pertes,"unité(s) d'eau")
    return nb_eau
  
def pluie(nb_eau:int,difficulté:int,nb_reservoir_eau:int):
    """fonction qui détérmine l'impacte d'une pluie sur le nb_eau en fonction de la difficulté et du nb de reservoir d'eau (batiment) construit"""
    gain=random.randint(10,30-2*difficulté) #on gagne une quantité d'eau selon la difficulté
    nb_eau=nb_eau+gain+(gain//2)*nb_reservoir_eau #la pluie apporte un certain gain et si construit chaque reservoir va aussi rapporter ce même
    print("Une forte pluie vous apporte",gain+(gain//2)*nb_reservoir_eau,"unité(s) d'eau")
    if nb_reservoir_eau >=1:
        print("Les reservoirs d'eau vous ont permis de récupérer",(gain//2)*nb_reservoir_eau,"unité(s) d'eau de plus")
    return nb_eau
    
def events(nb_eau:int,difficulté:int,nb_reservoir_eau:int):
    """fonction qui détérmine quand et quel événement va apparaître"""
    apparition_événement=random.randint(1,3)
    if apparition_événement==1: #Une chance sur trois qu'un événément se produise à un tour
        quel_événement=random.randint(1,2) #On va changer le deuxieme terme en fonction du nombre d'événements que l'on a
        if quel_événement==1:
            nb_eau = sécheresse(nb_eau,difficulté)
        elif quel_événement==2:
            nb_eau = pluie(nb_eau,difficulté,nb_reservoir_eau)
    return nb_eau
