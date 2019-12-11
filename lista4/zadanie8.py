#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import time
def zadanie8(n):
    harmony =0
    for x in range(1,n+1):
        enty= 1/x
        harmony +=enty
    print("Suma do",n,"wyrazu: ",harmony)
start = time.time()
zadanie8(100000000)
end = time.time()
print(end-start,"sekund")


