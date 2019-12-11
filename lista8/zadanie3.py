#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import random
import os
def peselgenerator(n):
    filetosave = open("PESEL.txt","w+")
    for i in range(n):
        year = random.randint(1900,2019)
        month = random.randint(1,12)
        if month == 2:
            day = random.randint(1,28)
        if month in (1, 3, 5, 7, 8, 10, 12):
            day = random.randint(1,31)
        if month in (4 ,6 , 9, 11):
            day = random.randint(1,30)
        if year<2000:
            if month>=10:
                month = str(month)
                c = month[0]
                d = month[1]
            if int(month)<10:
                month = str(month)
                c = "0"
                d = month[0]
        if year>=2000:
            month+=20
            month= str(month)
            c = month[0]
            d = month[1]
        year = str(year)
        a = year[2]
        b = year[3]
        if day<10:
            day = str(day)
            e = '0'
            f = day[0]
        if int(day)>=10:
            day = str(day)
            e = day[0]
            f = day[1]
        g = random.randint(0, 9)
        h = random.randint(0, 9)
        i = random.randint(0, 9)
        j = random.randint(0 , 9)
        k = ((int(a)*9)+(int(b)*7)+(int(c)*3)+int(d)+(int(e)*9)+(int(f)*7)+(g*3)+h+(i*9)+(j*7))%10
        g,h,i,j,k = str(g),str(h),str(i),str(j),str(k)
        Pesel = a+b+c+d+e+f+g+h+i+j+k
        filetosave.write(Pesel+"\n")
        print(Pesel)

peselgenerator(10)