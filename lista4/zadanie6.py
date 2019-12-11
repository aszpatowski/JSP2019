#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie6(r,g,b):
    import colorsys
    hsv = colorsys.rgb_to_hsv(r,g,b)
    print(hsv)
r = float(input("R: "))
g = float(input("G: "))
b = float(input("B: "))
zadanie6(r,g,b)