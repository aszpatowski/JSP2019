#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import SzyfrCezara as szyfr
tekst = input("Podaj tekst do zaszyfrowania")
klucz = int(input("Podaj klucz"))
print(szyfr.encrypted(tekst,klucz))
tekst = input("Podaj tekst do odszyfrowania")
klucz = int(input("Podaj klucz"))
print(szyfr.decrypted(tekst,klucz))