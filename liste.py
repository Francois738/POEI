#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import random
tableau_jeu=[]
# Liste de 10 éléments
for i in range (0,10):
    tableau_jeu.append (random.randint (1,10))
# On trie le tableau
tableau_jeu.sort ()
saisie=int (input ("Nombre entre 1 et 10 :"))
# Position dans le tableau
pos = 0
# Longueur du tableau
lg_tableau_jeu = len (tableau_jeu)
# Tant que la valeur n'a pas été trouvée
while ((pos < lg_tableau_jeu ) and ( tableau_jeu [pos] < saisie)):
    pos += 1
if ( tableau_jeu [pos] == saisie ):
    print ("Gagné")
else:
    print ("Perdu")
print ("\nContrôle visuel")
# Contrôle
for tirage in tableau_jeu:
    print (tirage,end=',')
print()
