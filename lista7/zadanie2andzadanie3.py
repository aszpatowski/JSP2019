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
    return A
def bubble_sort(A):
    n = len(A)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if A[j]>A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
    return A
A=[]
B=[]
C=[]
for i in range(0,100):
    A.append(random.randint(0,20))
for i in range(0,200):
    B.append(random.randint(0,20))
for i in range(0,300):
    C.append(random.randint(0,20))
A1 = A[:]
B1 = B[:]
C1 = C[:]
print("InsertSort: ")
start = time.time()
print(insert_sort(A))
end = time.time()
print(end-start,"sekund")
start = time.time()
print(insert_sort(B))
end = time.time()
print(end-start,"sekund")
start = time.time()
print(insert_sort(C))
end = time.time()
print(end-start,"sekund")
print("Bubblesort: ")
start = time.time()
print(bubble_sort(A1))
end = time.time()
print(end-start,"sekund")
start = time.time()
print(bubble_sort(B1))
end = time.time()
print(end-start,"sekund")
start = time.time()
print(bubble_sort(C1))
end = time.time()
print(end-start,"sekund")
