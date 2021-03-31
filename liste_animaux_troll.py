#!/usr/bin/python3
# -*- coding :utf-8 -*-

liste_animaux = ["lapin","chat", "chien", "chiot", "dragon", "ornithorynque"]
liste_animaux.append ("troll")
for animal_del in (("lapin","chat","chien","chiot")):
    liste_animaux.remove (animal_del);
for animal in liste_animaux:
    print (animal)
