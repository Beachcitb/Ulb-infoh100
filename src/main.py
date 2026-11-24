"""centralise le code et créer la boucle de jeux"""

import create_map
import events
import manage_bat
import afficher_histoire
import ui
import manage_ressources
import manage_population
import json
import random 
import choix_joueur
def main():
    """ce charge de tous mettre ensemble dans une boucle de jeux"""
    #afficher_histoire.introduction("histoire_ecrite.txt")
    seed = ui.ask_seed()
    with open("ressources.json","w") as info:
        json.dump({"seed":seed},info)
    random.seed(seed)
    ferme = create_map.create_map()#la ferme/map 
    while True :#conditions temporaire , mais ce qui nous fait perdre c'est si on a plus d'eau ou d'énergie
        create_map.afficher_map(ferme)
        if choix_joueur.action_selectionner(ui.afficher_action()) == 0:
            break
    

    
    
main()

