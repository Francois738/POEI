#!/usr/bin/env python

from random import randrange
from math import ceil

# Déclaration des variables 
argent = 1000 
continuer_partie = True #boleen vrai 

print (" Bienvenu dans le casino de la chance avec", argent,"€.")

while continuer_partie : # Tant que la partie continu l'utilisateur doit saisir un nombre
    nombre_mise = -1
    while nombre_mise < 0 or nombre_mise > 49:
        nombre_mise = input (" Quel est le nombre que tu as choisi (entre 0 et 49): ")
        try :
            nombre_mise = int( nombre_mise )
        except ValueError :
            print (" Tu dois choisir un nombre ")
            nombre_mise = -1
            continue
        if nombre_mise < 0:
            print ("les nombres négatifs sont interdits")
        if nombre_mise > 49:
            print ("les nombres supérieur à 49 sont interdits")
                        
# sélectionne la somme à miser sur le nombre
    mise = 0
    while mise <= 0 or mise > argent :
        mise = input (" Quel est ta mise : ")
# On convertit la mise
        try :
            mise = int( mise )
        except ValueError :
            print (" Tu n'as pas saisi de nombre ")
            mise = -1
            continue
        if mise <= 0:
            print ("La mise saisie est négative ou nulle .")
        if mise > argent :
            print (" Tu n'as pas assez d'argent, il te reste que", argent ,"€")
#le nombre et la mise ont été sélectionné, on fait tourner la roulette de la chance
    numero_gagnant = randrange (50)
    print ("La roulette tourne!!!!!!!!!!!!!!et la bille s'arrête sur le numéro", numero_gagnant )
                                            
# le gain
    if numero_gagnant == nombre_mise :
        print ("Bravo! Tu ramasses", mise * 3,"€ !")
        argent += mise * 3
    elif numero_gagnant % 2 == nombre_mise % 2: # Même couleur
        mise = ceil ( mise * 0.5)
        print (" Tu as la bonne couleur. Tu prends", mise ,"€")
        argent += mise
    else :
        print ("Désolé mon vieux, la prochaine sera la bonne. Tu perds ta mise.")
        argent -= mise     
# On interrompt la partie si le joueur est ruiné
    if argent <= 0:
        print (" Tu n'as même plus 1€! Tu dois attendre ton RSA.")
        continuer_partie = False
    else :
# On affiche l'argent du joueur
        print (" Tu as dans les mains", argent ,"€")
        quitter = input (" Tu ne vas pas rentrer avec si peu? Quitter le casino (o/n) ? ")
        if quitter == "o" or quitter == "O":
            print (" Tu quitte le casino avec une misère ta femme va te tuer.")
            continuer_partie = False
                                                                    
