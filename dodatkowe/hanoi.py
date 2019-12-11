#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
x=0
def hanoi(n, source, buffer, target):
    if n == 1:
        target.append(source.pop())
        print (source, buffer, target)
    else:
        hanoi(n-1, source, target, buffer)
        target.append(source.pop())
        print (source, buffer, target)
        hanoi(n-1, buffer, source, target)
number = 10
a = ["source"]
b = ["buffer"]
c = ["target"]
for i in range(number):
    a.append(number-i)
print(a, b, c)
hanoi(number, a, b, c)