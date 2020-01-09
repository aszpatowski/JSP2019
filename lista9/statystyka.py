#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import sys
import os
import numpy as np
def zadanie2(dane):
    average = np.average(dane)
    mediana = np.median(dane)
    odchylenie = np.std(dane)
    print("Średnia: ", average)
    print("Mediana: ", mediana)
    print("Odchylenie standardowe: ", odchylenie)

if __name__ == "__main__":
    if sys.argv[1].endswith(".txt"):
        file = open(sys.argv[1],'r')
        lines = list(file.read().split('\n'))
        lines.pop()
        lines = list(map(int,lines))
        zadanie2(lines)
    else:
        zadanie2((list(map(int, sys.argv[1].split(',')))))
        print(sys.argv)

