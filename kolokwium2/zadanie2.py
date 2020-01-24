#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def licz(plik):
    plik = open(plik)
    text=plik.read()
    wyklucz = [',','.','?','!','\n',';','  ']
    for i in range(0,len(wyklucz)):
        text = text.replace(wyklucz[i],' ')
    text = text.lower()
    text = text.split()
    slowa =set(text[:])
    for i in slowa:
        print(i,text.count(i))
licz("text_na_zajecia.txt")