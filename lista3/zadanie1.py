#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie1():
    samo = "aąeęuioóy"
    litera = input("Podaj literę: ")
    litera = litera.lower()
    result= samo.find(litera)
    if result==-1:
        print("Jest to spółgłoska.")
    else:
        print("Jest to samogłoska.")
zadanie1()

