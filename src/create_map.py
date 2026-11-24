import random
import json

""" l'objectif de ce fichier est de créer la map et de gérer les differentes fonctions qui permettent de modifier celle-ci,  la map est créer aléatoirement mise a part si une seed est rentrer"""
def create_map(difficulty:int=1):
    """créer la map en fonction de la taille , la seed et la difficulté ( a un impact sur le nombre de ressources, 1 -> normal , 2-> difficile , 3-> désert , 4-> enfer)"""
    length = int(random.gauss(40,10)) #permet d'avoir des tailles vraiables , mais on part quand meme d'une valeur de ref arbitraire 
    height = int(random.gauss(40,10)) 
    map1 =[["." for i in range(length)] for j in range(height)]
    #céer des obstacles/ressources
    nb_or = int(random.gauss(20,5)-difficulty*random.randint(1,3))#resource rare qui apparait en bloc de 1 (ne son pas réunis)
    pos_or =  [(random.randint(0,height-1),random.randint(0,length-1)) for i in range(nb_or)]#il peut y'avoir deux fois la meme pos mais c'est pas grave cela reduit juest le nombre d'or et si length ou height <1 (ce qui est très rare alors il faut faire une fin spéciale (easter egg)

    nb_baiemagique = random.randint(4,6)-difficulty#+1 d'énergie par tour mais on peut les consommer totalement pour gagner de la place et +2 énergies mais alors elle ne donne plus rien
    with open("ressources.json","r") as fichier:
        data = json.load(fichier)
    data["nb_baiemagique"] = nb_baiemagique
    with open("ressources.json","w") as fichier:
        json.dump(data,fichier)
    pos_baiemagique = [(random.randint(0,height-1),random.randint(0,length-1)) for i in range(nb_baiemagique)]
    print(pos_or)
    for i in pos_or:
        x,y = i
        map1[x][y] = "#"
    for i in pos_baiemagique:
        #si la baie magique est au mm endroit que l'or alors c'est la baie magique d'or qui gagne +1 or par tour et
        # elle peut etre miné pour mettre fin au jeu , mais demande un outil special
        x,y = i
        map1[x][y] = "@"
        if i in pos_or:
               map1[x][y] = "§" 
    return map1
    
def afficher_map(Map:list):
    """permet d'afficher la map ainsi que les positions"""
    print("voici t'as ferme : # représente l'or qui peut etre miner, @ les baies qui donne de l'énergie par tour mais peuvent etre detruite pour en gagner plus d'un coup mais ne plus en gagner par tour\n")
    ligne = ""
    for j in range(len(Map[0])):#prends une ligne au hasard car de toute facon chaque lignes a la meme longeur     
        if j == 0:
            ligne += "   "+str(j)
        else:
            ligne += " "*(3-len(str(j)))+str(j)#affiche les positions du dessus
    print(ligne)
    ligne = ""
    for i in range(len(Map)):#affichage de la map 
        for j in range(len(Map[i])):
            if j == 0:
                ligne += str(i) + " "*(3-len(str(i)))
            ligne += Map[i][j] + "  "#double espace nécéssaire car permet de garder un alignement avec les chiffres des pos
        print(ligne.rstrip())
        ligne = ""
