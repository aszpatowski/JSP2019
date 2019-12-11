#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie2(x,*args):
    w = 0
    for a in range(0,len(args)):
        w+=args[a]*x**a
    print(w)
zadanie2(2,2,2,2) # => x=2, a0=2,a1=2,a2=2
zadanie2(2,1,2,3,4,5)
