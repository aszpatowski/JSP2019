import os
from textwrap import wrap
def podziel(plik,ile):
    plik = open(plik)
    text=plik.read()
    a= wrap(text, ile)
    filetosave = open("./zapisz.txt",'w+')
    for x in range(0,len(a)):
        filetosave.write(a[x]+"\n")
podziel("text_na_zajecia.txt",30)