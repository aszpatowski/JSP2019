#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
# do 3 tysiecy
# sprawdz czy jest sens
def Check(num):
    wartosc = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    symbol = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    wynik = ''
    i = 0
    while num > 0:
        for _ in range(num // wartosc[i]):
            wynik += symbol[i]
            num -= wartosc[i]
        i += 1
    return wynik
def zadanie3(num):
    num = num.upper()
    rzymskie = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    wynik = 0
    try:
        for i in range(len(num)):
            if (i+1) == len(num) or rzymskie[num[i]] >= rzymskie[num[i+1]]:
                wynik += rzymskie[num[i]]
            else:
                wynik -= rzymskie[num[i]]
        if num == Check(wynik):
            return wynik
        else:
            wynik = "Niepoprawny zapis"
            return wynik

    except:
        wynik = "Niepoprawne cyfry rzymskie!"
        return wynik
print(zadanie3("mmii"))
print(zadanie3("icmm"))
print(zadanie3("MDCCCXCIX"))
print(zadanie3("idmm"))
print(zadanie3("MCDXCIX"))

