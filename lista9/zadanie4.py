#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
def wykresy():
    languages =["Java","C","Python","C++","C#","Visual Basic .NET","JavaScript","PHP","SQL","Swift"]
    values = [17.253,16.086,10.308,6.196,4.801,4.743,2.090,2.048,1.843,1.490]
    plt.bar(languages,values)
    plt.title('Najpopularniejsze języki programowania')
    plt.show()
wykresy()