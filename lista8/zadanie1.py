#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import os
import datetime
def encrypted(tekst,klucz):
    alphabet = "abcdefghijkmnolpqrstuvwxyzabcdefghijkmnolpqrstuvwxyz"
    ALPHABET = "ABCDEFGHIJKMNOLPQRSTUVWXYZABCDEFGHIJKMNOLPQRSTUVWXYZ"
    lista =[]
    for i in range(0,len(tekst)):
        lista.append(tekst[i])
        try:
            a= alphabet.index(lista[i])
            lista[i] = alphabet[a+klucz]
        except:
                try:
                    a = ALPHABET.index(lista[i])
                    lista[i] = ALPHABET[a + klucz]
                except:
                    pass
    tekst = "".join(lista)
    return tekst
def takefile(namefile):
    try:
        file = open(namefile)
        text = file.read()
    except FileNotFoundError:
        print("Błąd odczytu pliku: ",namefile," . Prawdopodobnie plik nie istnieje.")
        return 0
    file.close()
    n = int(input("Podaj przesunięcię od 1-10."))
    encryptedtext = encrypted(text,n)
    katalog = input("Podaj katalog do zapisania: ")
    if not os.path.exists(katalog):
        try:
            os.mkdir(katalog)
            print("Katalog ", katalog, " stworzony.")
        except:
            print("Błąd w tworzeniu.")
            return 0
    else:
        print("Katalog istnieje i zostanie zapisany w tym katalogu.")
    try:
        filetosave =open("{}/plik_zaszyfrowany{}_{}-{}-{}.txt".format(katalog,n, datetime.datetime.now().year, datetime.datetime.now().month,datetime.datetime.now().day), "x")
        filetosave.write(encryptedtext)
        print("Plik poprawnie zaszyfrowany i zapisany.")
    except:
        print("Błąd w zapisie pliku")
        return 0
takefile("plik_do_szyfrowania.txt")





