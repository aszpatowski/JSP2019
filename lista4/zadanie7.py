#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie7():
    N = int(input("Ilość wierszy: "))
    lista = []
    for n in range(1, N + 1):
        lista.append(1)
        for i in range(n - 2, 0, -1):
            lista[i] += lista[i - 1]
        print("N: ", n, lista)
zadanie7()