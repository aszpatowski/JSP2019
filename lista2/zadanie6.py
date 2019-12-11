#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
def zadanie6():
    lista_studentow = ["Kasia","Basia","Marek","Darek"]
    print("Lista studentów: ",lista_studentow)
    lista_studentow.extend(("Ania","Basia")) ##Dodawanie Ani i Basi
    print("Zaaktualizwana lista studentow: ",lista_studentow)
    lista_studentow.sort() ##sortowanie listy studentow
    print("Posortowana lista studentów: ",lista_studentow)
    print("4 student:",lista_studentow[3]) #wyswietla 4 studenta
    print("2 pierwszych studentów: ", lista_studentow[:2]) #wyswietla 2 pierwszych
    print("2 ostatnich studentów: ", lista_studentow[-2:]) #wyswietla 2 ostatnich
    while 1>0:
        try:
            lista_studentow.remove("Basia")
        except:
            break
    print("Po usunięciu wszystkich Basii: ",lista_studentow)
    print("Liczba studentów: ",len(lista_studentow))
    lista_studentow = tuple(lista_studentow)
    print("Lista przekonwertowana na tuple: ",type(lista_studentow),lista_studentow)
zadanie6()