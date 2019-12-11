#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import os
def zadanie4():
    try:
        pesel = open("PESEL.txt","r")
    except:
        print("Błąd odczytu")
    namefiletosave = "danezpesel.txt"
    filetosave = open(namefiletosave, "w+")
    for x in pesel.readlines():
        x = str(x)
        check = ((int(x[0])*9)+(int(x[1])*7)+(int(x[2])*3)+(int(x[3]))+(int(x[4])*9)+(int(x[5])*7)+(int(x[6])*3)+(int(x[7]))+(int(x[8])*9)+(int(x[9])*7))%10
        if check != int(x[10]):
            print("Pesel nieprawidłowy")
        else:
            if int(x[2]) in (2,3):
                year = int("20"+x[0:2])
                print(year)
                if int(x[2]) == 3:
                    month = "1"+x[3]
                else:
                    month = "0"+x[3]
            else:
                year = int("19"+x[0:2])
                month = x[2:4]
            day = x[4:6]
            if int(x[9])%2==0:
                plec = "kobieta"
            else:
                plec = "mężczyzna"
            print(year,"\n",month,"\n",day,"\n",plec)
            filetosave.write( "nr {}:\n data urodzenia: {}-{}-{};\t płeć: {}\n\n".format(x[0:11],day,month,str(year),plec))
zadanie4()


