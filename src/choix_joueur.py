import ui

def action_selectionner(choix:str):
    """performe une fonction spécifique ex constuire un batiment etc.. en fonction du choix du joueur"""
    """si la fonction retourne 0 cela veut dire que c'est un arret brutal"""
    match choix:
        case "f":#fin de partie
            return 0
        case "$":#achat 
            return 1
        case "b":#batiments
            return 1
        case "a":#actions
            return 1
        case "s":#stop du tour
            return 1
        case _:
            print("valeur entré n'est pas valide")
            action_selectionner(ui.afficher_action())
