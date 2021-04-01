#!/usr/bin/env python
# -*- coding:Utf-8 -*-

celsius, fahrenheit = 0, 32

fahrenheit = input("Donnez une température en fahrenheit :\n")
celsius = (fahrenheit - 32) / 1.8
    print fahrenheit, "Fh° valent", celsius, "C°"

celsius = input("Donnez une température en Celsius :\n")
fahrenheit = (celsius * 1.8) + 32
    print celsius, "C° valent", fahrenheit, "Fh°"
