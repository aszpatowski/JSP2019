#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
class Investment:
    def __init__(self, kwota_glowna,stopa_procentowa):
        self.p = kwota_glowna
        self.i = stopa_procentowa
    def Zysk(self,n):
        odsetki = self.p*(1+(self.i/100))**n # Zwraca cała wartość inwestycji, razem z kwotą glowną.
        print(round(odsetki,2))
        return odsetki
    def __str__(self):
        return 'Kwota główna - {}, Stopa procentowa - {}%'.format(format((self.p), '.2f'),format((self.i),'.2f'))
    def wykres(self,n):
        zysk =[]
        years = []
        for j in range(1,n+1):
            zysk.append((self.p*(1+(self.i/100))**j)-self.p)
            years.append(j)
        years= (list(map(str,years)))
        fig, ax = plt.subplots()
        rects = ax.bar(years, zysk)
        plt.ylabel("Zysk [PLN]")
        plt.xlabel("Lata")
        plt.title('Zysk w ciągu {} lat.'.format(n))
        plt.show()
pieniazki = Investment(2000,5)
pieniazki.Zysk(1.3)
print(pieniazki)
pieniazki.wykres(10)
