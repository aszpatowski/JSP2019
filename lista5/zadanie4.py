#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie4(tekst,mode):
    key= {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}
    if mode=="de":
        key = {v: k for k, v in key.items()}
    encrypted = ''
    for i in tekst:
        if i in key:
            encrypted+=key[i]
        else:
            encrypted+=i
    print(encrypted)
    return encrypted
zadanie4(zadanie4("to jest moj tekst","en"),"de")