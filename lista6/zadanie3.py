#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
from itertools import groupby
def lookandsay(n):
    xn = '1'
    for x in range(0,n):
        print(x+1,". ",xn)
        xn= ''.join( str(len(list(g))) + k for k, g in groupby(xn))
    print(x + 2, ". ", xn)
n =int(input("Podaj n: "))
lookandsay(n)