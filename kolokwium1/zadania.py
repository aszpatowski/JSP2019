#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie1():
    import math
    print("Podaj współrzędne pierwszego punktu")
    x1=float(input("Podaj współrzędna x1: "))
    y1 = float(input("Podaj współrzędna y1: "))
    print("Podaj współrzędne drugiego punktu")
    x2 = float(input("Podaj współrzędna x2: "))
    y2 = float(input("Podaj współrzędna y2: "))
    a = x1-x2
    b=y1-y2
    c =math.sqrt(a**2+b**2)
    c = round(c,2)
    return c
def zadanie2(*argv):
    i= 0
    sum = 0
    for arg in argv:
        i+=1
        sum +=arg
    if i == 0:
        return i
    else:
        average = sum/i
        return average
def zadanie3(n):
    answer = None
    whatisnot =[]
    alphabet = "abcdefghijkmnolpqrstuvwxyz"
    for x in range(0,len(alphabet)):
        for y in range(0,len(n)):
            if alphabet[x]==n[y]:
                break
            if y ==len(n)-1:
                whatisnot.append(alphabet[x])
                answer= "Nie nie jest"
    if answer is None:
        answer="Jest"
    print(whatisnot)
    return answer
##print(zadanie1())
#print(zadanie2())
#print(zadanie2(7,2,3))
print(zadanie3("The quick brown fox jumps over the lazy dog. False, i see false, this exam i may pass."))
print(zadanie3("The quick brown fox jumps over the  dog. False, i see false, this exam i may pass."))
print(zadanie3("The quick fox jumps over the lazy dog. False, i see false, this exam i may pass."))





