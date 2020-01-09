#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
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
            KwotaWaluta = (kwota*float((self.Course[index1]).replace(',','.'))/float((self.Course[index2]).replace(',','.')))*(int(self.Converter[index2])/int(self.Converter[index1]))
            print("{} {} to {} {}".format(kwota,KodWaluta1,KwotaWaluta,KodWaluta2))
            return KwotaWaluta
        except:
            print("Kody walut są niepoprawne.")
kursy = Kursy('kursy/a004z200108.xml')
kursy.ListaKursow()
kursy.PLNtoDiffrent(110,"eur")
kursy.DiffrentToDiffrent(125.10,'huf','czk')