#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def compare(x):
	return x[1]
def zadanie7():
    list =[(2,8),(5,5),(9,3),(1,0),(3,2),(6,4),(1,9),(10,3),(2,3),(1,7)]
    list=sorted(list,key=compare)
    print(list)
zadanie7()