#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie9():
    jnumber = int(input("ilość kolumn: "))
    inumber = int(input("ilość wierszy: "))
    i=[]
    j=[]
    for x in range(1,inumber+1):
        i.append(x)
    for x in range(1,jnumber+1):
        j.append(x)
    print("",end="\t\t")
    for x in range(0,len(j)):
        print(j[x],end="\t")
    print("","\n\n")
    for x in range(0,len(i)):
        print(i[x], end="\t\t")
        for y in range(0,len(j)):
            print(j[y]*i[x],end="\t")
            if y ==(len(j)-1):
                print("",end="\n\n")
zadanie9()