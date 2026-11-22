import time
def introduction(fichier):
    """imprime l'histoire present de le dir histoire avec un certain temps entre chaque phrase pour le rendre plus naturel"""
    with open(fichier,mode ="r",encoding="utf-8") as histoire:
        for line in histoire:
            if line != "\n":
                print(line)
                time.sleep(0.04*len(line))#vaire en fonction de la longeur de la phrase pour que ce soit plus naturel
            else:
                continue
            



