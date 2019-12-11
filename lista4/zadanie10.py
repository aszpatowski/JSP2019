#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie10(a, b):
    while b!=0:
        r = a%b
        a = b
        b = r
    print("NWD: ",a)
    return a
zadanie10(95,105)
