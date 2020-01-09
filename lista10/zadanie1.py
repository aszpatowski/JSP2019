#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import numpy as np
class Kolo:
    def __init__(self, r):
        self.pole = (r*r)*np.pi
        self.obwod = 2*np.pi*r
circle = Kolo(10)
print(circle.pole)
print(circle.obwod)
class Unpacked:
    def __init__(self, lista):
        sublist = [[]]
        for i in range(len(lista) + 1):
            for j in range(i + 1, len(lista) + 1):
                sub = lista[i:j]
                sublist.append(sub)
        self.sublists = sublist
lista = [1,2,3]
lista1 = [1,2,3,"hej","co tam"]
listadopodlisty = Unpacked(lista)
listadopodlisty2 = Unpacked(lista1)


#print(listadopodlisty.sublists)
#print(listadopodlisty2.sublists)

class Unpacked3sum0:
    def __init__(self, lista):
        sublist = []
        for i in range(len(lista) + 1):
            for j in range(i + 1, len(lista) + 1):
                sub = lista[i:j]
                sublist.append(sub)
        for i in range(len(sublist)-1, -1,-1):
            if len(sublist[i])!=3:
               sublist.pop(i)
        for i in range(len(sublist) - 1, -1, -1):
            if sum(sublist[i]) != 0:
                sublist.pop(i)
        self.sublists = sublist
listasuper = [1,2,-3,-1,3,-2,1,-1,-2.5,2,0.5]
listadopodlistysuper  = Unpacked3sum0(listasuper)
print(listadopodlistysuper.sublists)