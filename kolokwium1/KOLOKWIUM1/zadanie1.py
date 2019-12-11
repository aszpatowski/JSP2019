#!/usr/bin/python3.6
#-*- coding: utf-8 -*-

import math
import itertools
lista = [2,(17,-8),6,"Ala","Python",-4.0,"Ela"]
lista1 = [-2,[-17,8],"Najdłuższy stringggg","jola",-5,1000, 10.00]
def zadanie1(lista):
    longeststring = ""
    minnumber = math.inf
    for x in range(0,len(lista)):
        if type(lista[x])==list or type(lista[x])==tuple or type(lista[x])==set:
            unpacked=list(itertools.chain(lista[x]))
            lista.remove(lista[x])
            for y in range(0,len(unpacked)):
                lista.append(unpacked[y])
    for x in range(0,len(lista)): #druga pętla zastosowana jest dlatego, że długość listy ulega zmianie po rozpakowaniu.
        if type(lista[x])==str:
            if len(lista[x])>len(longeststring):
                longeststring = lista[x]
        if type(lista[x])==int or type(lista[x])==float or type(lista[x])==complex:
            if lista[x]<minnumber:
                minnumber = lista[x]
    print("Najdłuższy łańcuch to: ",longeststring,  "\nNajmniejsza liczba to: ",minnumber)


zadanie1(lista)
zadanie1(lista1)



