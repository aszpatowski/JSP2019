#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie2():
    number =int(input("Podaj liczbę całkowitą: "))
    if number%2==0:
        print("Jest to liczba parzysta.")
    else:
        print("Jest to liczba nieparzysta.")
def zadanie2a():
    number = int(input("Podaj liczbę całkowitą: "))
    Typ = ("Jest to liczba parzysta.","Jest to liczba nieparzysta.")
    print(Typ[number%2])
zadanie2()
zadanie2a()