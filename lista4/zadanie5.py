#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie5():
    from itertools import permutations
    lista = ['a','b',1,2,3]
    permutacja=list(permutations(lista))
    for x in list(permutacja):
        print(x)
zadanie5()