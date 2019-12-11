#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import math
import random
import time
def merge(A,p,q,r):
    n1= q-p+1
    n2=r-q
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0,n1):
        L[i]=A[p+i]
    for j in range(0,n2):
        R[j]=A[q+j+1]
    L.append(math.inf)
    R.append(math.inf)
    i =0
    j=0
    k=p
    for k in range(p,r+1):
        if L[i]<=R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
def mergeSort(A,p,r):
    if p<r:
        q = (p+r-1)//2
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)
N= int(input("Podaj ilość elementów w liscie: "))
A =[random.randrange(1,10000,1) for i in range(N)]
B =A[:]
print("Nieposortowana:",A,"\n")
start = time.time()
print(mergeSort(A,0,len(A)-1))
end = time.time()
print(end-start,"sekund.")
B= sorted(B)
print(B)
print("\nPosortowana: ",A)
