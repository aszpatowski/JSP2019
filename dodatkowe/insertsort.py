#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import random
import time
def insert_sort(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i - 1
        while j>=0 and A[j]>key:
            A[j+1]=A[j]
            j-=1
        A[j + 1] = key
N= int(input("Podaj ilość elementów w liscie: "))
A =[random.randrange(1,10000,1) for i in range(N)]
print("Nieposortowana:",A,"\n")
start = time.time()
insert_sort(A)
end = time.time()
print(end-start,"sekund.")
print("\nPosortowana: ",A)