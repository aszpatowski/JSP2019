#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import time
def fiboiteracja(n):
    fibo=[0,1]
    for i in range(2,n):
        fibo.append(fibo[i-1]+fibo[i-2])
    return fibo[n-1]
def fiborecursion(n):
    if n <= 1:
        return n
    else:
        return (fiborecursion(n - 1) + fiborecursion(n - 2))
start = time.time()
print(fiboiteracja(10))
end = time.time()
print(end-start,"sekund")
start = time.time()
print(fiborecursion(9))
end = time.time()
print(end-start,"sekund")