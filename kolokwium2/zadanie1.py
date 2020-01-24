#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def podziel(plik):
    plik = open(plik)
    text=plik.read()
    nowy = text.split('.')
    if(nowy[len(nowy)-1]=='\n' or nowy[len(nowy)-1]==''):
        nowy.pop(len(nowy)-1)
  #  print(text)
   # print("\n\n")
  #  print(nowy)
    print('Ilość zdań: ',len(nowy))
podziel("text_na_zajecia.txt")