#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie7():
    fibo = [0,1]
    N= int(input("Podaj N: "))
    while 1>0:
        a = fibo[-1]+fibo[-2]
        fibo.append(a)
        if N<fibo[-1]:
            del fibo[-1]
            break
    print(fibo)
zadanie7()