#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie1(s):
    Liczby= {
        "jeden" : 1,
        "dwa" : 2,
        "trzy" : 3,
        "cztery" : 4,
        "pięć" : 5,
        "sześć" : 6,
        "siedem" : 7,
        "osiem" : 8,
        "dziewięć" : 9,
        "dziesięć" : 10,
        "jedenaście" : 11,
        "dwanaście" : 12,
        "trzynaście" : 13,
        "czternaście" : 14,
        "pietnaście" : 15,
        "szesnaście" : 16,
        "siedemnaście" : 17,
        "osiemnaście" : 18,
        "dziewiętnaście" : 19,
    }
    Dziesiatki ={
        "dwadzieścia" : 20,
        "trzydzieści" : 30,
        "czterdzieści" : 40,
        "pięćdziesiąt" : 50,
        "sześćdziesiąt" : 60,
        "siedemdziesiąt" : 70,
        "osiemdziesiąt" : 80,
        "dziewięćdziesiąt" : 90
    }
    s = s.lower()
    a = s.split(" ")
    try:
        x = Dziesiatki[a[0]]
        try:
            y = Liczby[a[1]]
            z = x+y
            print(z)
            return z
        except:
            print(x)
            return x
    except:
        x = Liczby[a[0]]
        print(x)
        return x
assert (zadanie1("jeden"))==1
assert (zadanie1("trzydzieści trzy"))==33
assert (zadanie1("trzynaście"))==13