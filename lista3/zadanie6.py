#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie6():
    j=[1,2,3,4,5,6,7,8,9,10]
    inumber = int(input())
    i=[]
    for x in range(1,inumber+1):
        i.append(x)
    print("",end="\t")
    for x in range(0,len(j)):
        print(j[x],end="\t\t")
    print("","\n")
    for x in range(0,len(i)):
        print(i[x], end="\t\t")
        for y in range(0,len(j)):
            print(j[y]*i[x],end="\t")
            if y ==(len(j)-1):
                print("",end="\n\n")
zadanie6()