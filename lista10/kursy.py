#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from os import system
class Kursy:
    def __init__(self,source):
        mytree = ET.parse(source)
        myroot = mytree.getroot()
        self.Name = ['Polski Złoty']
        self.Converter = [1]
        self.Code = ['PLN']
        self.Course = ['1,0000']
        for x in myroot:
            if x.tag == 'pozycja':
                self.Name.append(x[0].text)
                self.Converter.append(x[1].text)
                self.Code.append(x[2].text)
                self.Course.append(x[3].text)
    def ListaKursow(self):
        print("Lista Dostępnych kursów: \n")
        print("Nazwa Waluty", "Przelicznik", "Kod Waluty", "Kurs Średni", sep="\t\t\t",end='\n\n')
        for x in range(0,len(self.Name)):
            print(self.Name[x],end="")
            for y in range(0,(35-len(self.Name[x]))): #Aby choć troche tabela była rowna(35 bo tyle znakow ma najdluzszy string)
                print(' ',end='')
            if(int(self.Converter[x])>100):
                print(self.Converter[x], '{}\t'.format(self.Code[x]), self.Course[x], sep="\t\t")
            else:
                print(self.Converter[x],self.Code[x],self.Course[x],sep="\t\t\t")
    def PLNtoDiffrent(self,kwota,KodWaluta):
        KodWaluta = KodWaluta.upper()
        try:
            index = self.Code.index(KodWaluta)
            KwotaWaluta = (kwota/float((self.Course[index]).replace(',','.')))*int(self.Converter[index])
            print("{} PLN to {} {}".format(kwota,KwotaWaluta,KodWaluta))
            return KwotaWaluta
        except:
            print("Kod waluty jest niepoprawny")
    def DiffrentToDiffrent(self,kwota,KodWaluta1,KodWaluta2):
        KodWaluta1 = KodWaluta1.upper()
        KodWaluta2 = KodWaluta2.upper()
        try:
            index1 = self.Code.index(KodWaluta1)
            index2 = self.Code.index(KodWaluta2)
            KwotaWaluta = (kwota*float((self.Course[index1]).replace(',','.'))/float((self.Course[index2]).replace(',','.')))*int(self.Converter[index2])/int(self.Converter[index1])
            print("{} {} to {} {}".format(kwota,KodWaluta1,KwotaWaluta,KodWaluta2))
            return KwotaWaluta
        except:
            print("Kody walut są niepoprawne.")
def program_do_przeliczania_walut():
    kursy = Kursy('kursy/a004z200108.xml')
    while(True):
        try:
            print("Co chcesz zrobić?","1. Wyświetlić listę dostępnych kursów","2. Konwersja PLN na wybraną walutę","3. Konwersja wybranej waluty na inna walutę","4. Wyjście",sep="\n")
            wybor=int(input(": "))
            system("clear")
            if(wybor==1):
                kursy.ListaKursow()
            if(wybor==2):
                print("\n")
                kursy.PLNtoDiffrent(float(input("Podaj kwotę: ")),input("Podaj kod waluty: "))
                print("\n")
            if(wybor==3):
                print("\n")
                kursy.DiffrentToDiffrent(float(input("Podaj kwotę: ")), input("Podaj kod waluty w której jest kwota: "), input("Podaj kod waluty docelowej: "))
                print("\n")
            if(wybor==4):
                break
        except:
            system("clear")
            print("Podane wartości nie były liczbami lub kody walut były niepoprawne.")
program_do_przeliczania_walut()