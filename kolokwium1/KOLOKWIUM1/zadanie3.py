#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie3(pierwsze,drugie):
    pierwsze = pierwsze.lower()
    drugie = drugie.lower()
    if(sorted(pierwsze)==sorted(drugie)):
        print("To jest anagram")
    else:
        print("To nie jest anagram")
pierwsze = input("Podaj pierwsze słowo: ")
drugie = input("Podaj drugie słowo: ")
zadanie3(pierwsze,drugie)

