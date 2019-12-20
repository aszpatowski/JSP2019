#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import numpy as np
import random
M = 100
N =10
lista1 = random.sample(range(M),N)
listaprzyklad = [10,8,3,6,4,2,1,5]
def zadanie1(lista):
    sorted_idx = sorted(range(len(lista)), key=lista.__getitem__)
    return sorted_idx
print(zadanie1(lista1))
assert (zadanie1(listaprzyklad))==[6, 5, 2, 4, 7, 3, 1, 0]