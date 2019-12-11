#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie10(a,b):
    liczby = []
    for i in range(a, b+1):
        ls = str(i)
        length = len(ls)
        for x in range(0,length):
            if (int(ls[x]) % 2 == 1):
                break
            if (int(ls[x]) % 2 == 0) and x ==length -1:
                liczby.append(i)
    print(liczby,end="\n")
zadanie10(100,40000)

