""" gére les évenements : ce qui ce passe et leurs probabilités """
import random
import json

with open("ressources.json","r") as info:
    liste_données=json.load(info)

difficulté=liste_données["difficulty"]

def sécheresse(nb_eau:int):
    """fonction qui détérmine les pertes du à la sécheresse selon la difficulté"""
    if nb_eau >= 8:
        pertes= random.randint(1,(nb_eau//2)//(5-difficulté)) #Avec difficulté de 1 à 4
        nb_eau = nb_eau - pertes
        print("Une période de sécheresse vous fait perdre",pertes,"unité(s) d'eau")
    else:# Si nb_eau < 8 alors (nb_eau//2)//(5-difficulté) peut donner 0 donc ici cas spécifique
        pertes=min(nb_eau,2*difficulté)
        nb_eau = nb_eau - pertes
        print("Une période de sécheresse vous fait perdre",pertes,"unité(s) d'eau")
    return nb_eau
  
def pluie(nb_eau:int,nb_réservoir_eau:int):
    """fonction qui détérmine l'impacte d'une pluie sur le nb_eau en fonction de la difficulté et du nb de reservoir d'eau (batiment) construit"""
    gain=random.randint(10,30-2*difficulté) #on gagne une quantité d'eau selon la difficulté
    nb_eau=nb_eau+gain+(gain//2)*nb_réservoir_eau #la pluie apporte un certain gain et si construit chaque reservoir va aussi rapporter la moitié
    print("Une forte pluie vous apporte",gain+(gain//2)*nb_réservoir_eau,"unité(s) d'eau")
    if nb_réservoir_eau >=1:
        print("Les réservoirs d'eau vous ont permis de récupérer",(gain//2)*nb_réservoir_eau,"unité(s) d'eau de plus")
    return nb_eau

def achat_engrais(nb_or:int,nb_engrais:int):
    """fonction qui propose au joueur d'acheter une quanitité aléatoire d'engrais tout les quelques tours pour un prix qui varie légèrement"""
    quantite_propose_engrais=random.randint(3,8)
    prix_propose_engrais=round(quantite_propose_engrais*random.uniform(0.50,1.5)) #random.uniform permet de générer un nombre aléatoire à virgule
    choix=input("Un marchand vous propose d'acheter " + str(quantite_propose_engrais)+" unité(s) d'engrais pour le prix de "+str(prix_propose_engrais)+" pièce(s) d'or? Acheter? \n Non: 1 \n Oui: 2 \n Réponse: ")
    while choix != "1" and choix != "2":
        choix=input("Mauvaise entrée, appuyer 1 pour non et 2 pour oui: ")
    if choix == "1":
        return nb_or,nb_engrais
    elif choix == "2":
        if nb_or < prix_propose_engrais:
            print( "Vous n'avez pas assez de pièce pour effectuer la transaction.")
            return nb_or,nb_engrais
        else:   
            nb_or=nb_or-prix_propose_engrais
            nb_engrais=nb_engrais+quantite_propose_engrais
            return nb_or,nb_engrais

def destruction(nb_or_initial:int,nb_engrais_initial:int,nb_eau_initial:int):
    """fonction qui détruit la ferme, mais a très peu de chance de se produire"""
    nb_or=nb_or_initial
    nb_engrais=nb_engrais_initial
    nb_eau=nb_eau_initial
    nb_réservoir_eau=0
    return nb_or,nb_engrais,nb_eau,nb_réservoir_eau
    
    
def events(nb_or:int,nb_engrais:int,nb_eau:int,nb_réservoir_eau:int):
    """fonction qui détérmine quand et quel événement va apparaître"""
    apparition_événement=random.randint(1,3)
    if apparition_événement==1: #Une chance sur trois qu'un événément se produise à un tour
        quel_événement=random.randint(1,2) #On va changer le deuxieme terme en fonction du nombre d'événements que l'on a
        if quel_événement==1:
            nb_eau = sécheresse(nb_eau)
            return nb_or,nb_engrais,nb_eau,nb_réservoir_eau
        elif quel_événement==2:
            nb_eau = pluie(nb_eau,nb_réservoir_eau)
            return nb_or,nb_engrais,nb_eau,nb_réservoir_eau
    elif apparition_événement==2: #Une chance sur trois que le joueur soit proposé d'acheter de l'engrais
        nb_or,nb_engrais=achat_engrais(nb_or,nb_engrais)
        return nb_or,nb_engrais,nb_eau,nb_réservoir_eau
    elif apparition_événement==3: #renvoit les paramètres inchangés si aucun événement
        return nb_or,nb_engrais,nb_eau,nb_réservoir_eau
