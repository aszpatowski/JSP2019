#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import itertools
def zadanie9():
    a = [[2,4,3],[1,5,6],[9],[7,9,0]]
    b=list(itertools.chain(a[0],a[1],a[2],a[3]))
    print(b)
zadanie9()