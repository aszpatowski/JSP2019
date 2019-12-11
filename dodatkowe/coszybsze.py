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
def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = A[p + i]

    for j in range(0, n2):
        R[j] = A[q + 1 + j]

    i = 0
    j = 0
    k = p

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        A[k] = R[j]
        j += 110
        k += 1
def mergeSort(A, p, r):
    if p < r:
        q = (p + (r - 1)) // 2
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)
N= int(input("Podaj ilość elementów w liscie: "))
A =[random.randrange(1,10000,1) for i in range(N)]
B =[a for a in A]
print("Nieposortowana:",A,"\n")
start = time.time()
insert_sort(A)
end = time.time()
print(end-start,"sekund.")
print("\nPosortowana: ",A)
print("Nieposortowana:",B,"\n")
start = time.time()
n = len(B)
mergeSort(B, 0, n - 1)
end = time.time()
print(end-start,"sekund.")
print("\nPosortowana: ",B)

