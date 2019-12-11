#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie3():
    import math
    print("Rodam Ci pierwiatki równania kwadratowego w formacie ax^2+bx+c=0 .")
    a = int(input("Podaj a: "))
    if a==0:
        print("To nie jest równanie kwadratowe!")
    else:
        b = int(input("Podaj b: "))
        c = int(input("Podaj c: "))
        delta = (b**2)-(4*a*c)
        if delta<0:
            print("Równanie nie ma pierwiastków")
        elif delta==0:
            x = -b / 2 * a
            print("Pierwiastkiem równania jest: ",x)
        else:
            x1 = (-b - math.sqrt(delta))/ 2 * a
            x2 = (-b + math.sqrt(delta))/ 2 * a
            print("Pierwiastkami równania są: ",x1,x2)

zadanie3()