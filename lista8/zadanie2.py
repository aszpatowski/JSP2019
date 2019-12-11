#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import os
import datetime
def decrypted(tekst,klucz):
    klucz = klucz*(-1)
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
def takedir():
    dirfile = input("Podaj scieżke katalogu do odszyfrowania np. katalog:  ")
    try:
        for namefile in os.listdir(dirfile):
            if namefile.startswith("plik_zaszyfrowany"):
                if namefile[19]=='_':
                    n = namefile[17:19]
                else:
                    n =namefile[17]
                try:
                    n=int(n)
                    file = open(dirfile+"/"+namefile)
                    text = file.read()
                except FileNotFoundError:
                    print("Błąd odczytu pliku: ", namefile, " . Prawdopodobnie plik nie istnieje.")
                    return 0
                file.close()
                decryptedtext = decrypted(text, n)
                try:
                    filetosave = open("{}/plik_deszyfrowany{}_{}-{}-{}.txt".format(dirfile, n, datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day), "x")
                    filetosave.write(decryptedtext)
                    print("Plik poprawnie zaszyfrowany i zapisany.")
                except:
                    print("Błąd w zapisie pliku")
                    return 0
    except:
        print("Błąd odczytu katalogu",dirfile,". Prawdopodobnie katalog nie istnieje.")
        return 0
takedir()