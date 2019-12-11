#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie5():
    import re
    passw= input("Wpisz hasło: ")
    check = True
    while check:
        if (len(passw) < 6 or len(passw) > 16):
            print("Niepoprawne hasło. Zła ilość znaków.")
            break
        elif not re.search("[a-z]", passw):
            print("Niepoprawne hasło. Brak małej litery.")
            break
        elif not re.search("[A-Z]", passw):
            print("Niepoprawne hasło. Brak duzej litery.")
            break
        elif not re.search("[0-9]", passw):
            print("Niepoprawne hasło. Brak cyfry.")
            break
        elif not re.search("[$#@]", passw):
            print("Niepoprawne hasło. Brak znaku specjalnego.")
            break
        else:
            print("Poprawne hasło!")
            check= False
zadanie5()