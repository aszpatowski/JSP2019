#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie10():
    lista = []
    for x in range(3,100,3):
        lista.append(x)
    print("Lista z podpunktu 1: ",lista)
    leng = len(lista)-1
    for y in range(4,leng,2):
        try:
            del lista[y]
        except:
            break
    print("Lista z podpunktu 2: ",lista)
    average = sum(lista)/len(lista)
    print("Średnia z podpunktu 3: ",average)
zadanie10()