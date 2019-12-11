#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie1():
    krotka = (1, "a",2,"b")
    napis = "".join(krotka)
    print(napis)
    print(type(napis))
def zadanie2():
    list = [1,1,2,4,6,5,3,1]
    max = -5000
    min = 5000
    for x in range(0,len(list)):
        y = list[x]
        if y>max:
            max = y
            ind_max = x
        if y<min:
            min = y
            ind_min = x
    print("index max: ",ind_max)
    print("index min: ", ind_min)
zadanie1()
print("\n","\n","\n")
zadanie2()
