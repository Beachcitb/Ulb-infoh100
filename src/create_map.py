import random
""" l'objectif de ce fichier est de créer la map et de gérer les differentes fonctions qui permettent de modifier celle-ci,  la map est créer aléatoirement mise a part si une seed est rentrer"""
def create_map(seed:int=None,difficulty:int=1):
    """créer la map en fonction de la taille , la seed et la difficulté ( a un impact sur le nombre de ressources, 1 -> normal , 2-> difficile , 3-> désert , 0-> paradis)"""
    random.seed(seed)#si la seed est set to None ne pas faire de seed et la map est random
    length = 400 #juste des valeurs arbitraires qu'on peut changer au cours du temps
    height = 400
    map1 =[["." for i in range(length)] for j in range(height)]#cette map est pas affichable en soi(c'est juste un test)
    return map1

