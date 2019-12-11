#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie9(n):
    f = 1
    for x in range(1,n+1):
        f*=x
    print("Silnia do",n,"wyrazu to: ",f)
n = int(input("N: "))
zadanie9(n)