#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie1():
    lista =[]
    a = [0,10,8,3,5,4,7]
    b = len(a)
    for x in range(0,b):
        c= int(a[x])
        if c%2==1:
            lista.append(c)
    print(lista)
zadanie1()
def zadanie2():
    N = int(input("Podaj liczbę: "))
    for x in range(0,N):
        print('*'*x)
    for x in range(N,0,-1):
        print('*' * x)
zadanie2()