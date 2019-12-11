#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie2(n):
    Tysiace = {
        1000 : "tysiąc"
                }
    Setki = {
        100: "sto",
        200:"dwieście",
        300:"trzysta",
        400:"czterysta",
        500:"pięćset",
        600:"sześćset",
        700:"siedemset",
        800:"osiemset",
        900:"dziewiećset"
            }
    Dziesiatki = {
        "dwadzieścia": 20,
        "trzydzieści": 30,
        "czterdzieści": 40,
        "pięćdziesiąt": 50,
        "sześćdziesiąt": 60,
        "siedemdziesiąt": 70,
        "osiemdziesiąt": 80,
        "dziewięćdziesiąt": 90
    }
    Liczby = {
        "jeden": 1,
        "dwa": 2,
        "trzy": 3,
        "cztery": 4,
        "pięć": 5,
        "sześć": 6,
        "siedem": 7,
        "osiem": 8,
        "dziewięć": 9,
        "dziesięć": 10,
        "jedenaście": 11,
        "dwanaście": 12,
        "trzynaście": 13,
        "czternaście": 14,
        "pietnaście": 15,
        "szesnaście": 16,
        "siedemnaście": 17,
        "osiemnaście": 18,
        "dziewiętnaście": 19,
    }
    Liczby = {v: k for k, v in Liczby.items()}
    Dziesiatki = {v: k for k, v in Dziesiatki.items()}
    answer =None
    if n>1000:
        a = int(n/1000)*1000
        n = n%1000
        a = Tysiace[a]
        answer =a
    if n>100:
        b = int(n/100)*100
        n = n%100
        b = Setki[b]
        if answer is not None:
            answer+=" "+b
        else:
            answer = b
    if n>19:
        c = int(n/10)*10
        n = n%10
        c = Dziesiatki[c]
        if answer is not None:
            answer+=" "+c
        else:
            answer = c
    if n<=19:
        d = n
        d = Liczby[d]
        if answer is not None:
            answer+=" "+d
        else:
            answer = d
    print(answer)
    return answer
zadanie2(1024)
zadanie2(999)
assert(zadanie2(1511))=="tysiąc pięćset jedenaście"
assert(zadanie2(698))=="sześćset dziewięćdziesiąt osiem"