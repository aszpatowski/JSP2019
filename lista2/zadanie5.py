#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie5():
    textbegin = input("Podaj pierwszy napis: ")
    textmiddle = input("Podaj napis do wstawienia: ")
    length = int(len(textbegin))
    half = int(length/2)
    textend = textbegin[0:half]+textmiddle+textbegin[half:length]
    print(textend)
zadanie5()