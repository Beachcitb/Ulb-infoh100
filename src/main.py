"""centralise le code et créer la boucle de jeux"""

import create_map
import events
import manage_bat
import afficher_histoire
import ui
import manage_ressources
import manage_population

def main():
    """ce charge de tous mettre ensemble dans une boucle de jeux"""
    afficher_histoire.introduction("histoire_ecrite.txt")

main()

