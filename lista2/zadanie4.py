#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie4():
    napis = input("Podaj napis: ")
    a = napis[0]
    c = napis.replace(a,'$')
    c = c.replace('$',a,1)
    print(c)
zadanie4()