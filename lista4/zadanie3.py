#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie3(liczba,what):
    import math
    if what == "rad":
        print("Radians= ",liczba)
        print("Degrees= ", math.degrees(liczba))
    if what == "deg":
        print("Degrees= ",liczba)
        print("Radians= ", math.radians(liczba))
liczba = int(input("Liczba: "))
what = input("Jeśli podałeś liczbe w radianach, wpisz: rad.\n Jesli podales liczbe w stopnaich, wpisz: deg.\n: ")
zadanie3(liczba,what)
