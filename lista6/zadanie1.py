#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import trojkat as tr
check=True
while(check==True):
    a = float(input("Podaj wartość pierwszego boku: "))
    b = float(input("Podaj wartość drugiego boku: "))
    c = float(input("Podaj wartość trzeciego boku: "))
    checklist=sorted([a,b,c])
    if checklist[0]+checklist[1]>checklist[2]:
        check=False
    else:
        print("To nie jest trójkąt drogi użytkowniku.")
print("Obwod: ",tr.obwod(a,b,c))
print("Pole: ",tr.pole(a,b,c))
print("Jest to trójkąt: ",tr.jakitrojkat_boki(a,b,c))
print("Oraz: ",tr.jakitrojkat_katy(a,b,c))

