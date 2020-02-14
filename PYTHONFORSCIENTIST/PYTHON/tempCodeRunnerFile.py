import numpy
import matplotlib.pyplot as plt
whatplot = 0
for jakiSpin in range(0,2):
    if jakiSpin==0:
        n=10
        s=0.5
    if jakiSpin==1:
        whatplot=0
        n=6
        s=1
    for jakieh in range(0,5):
        if(jakieh==0):
            h=0
            whatplot=1
        if(jakieh==1):
            h=0.05
            whatplot=2
        if(jakieh == 2):
            h = 0.1
            whatplot=3
        if(jakieh == 3):
            h = 0.5
            whatplot=4
        if (jakieh == 4):
            h = 1
            whatplot=5
        #print(whatplot)
        plik_results = open(f"/home/aleksander/Pulpit/python/repos/JSP2019/PYTHONFORSCIENTIST/PYTHON/SPIN{s}/WSZYSTKO/resultsS{s}N{n}J1H{h}.txt")
        results = plik_results.readlines()
        del results[:(results.index("\n")+1)]
        del results[results.index("BRRRRUSH...\n"):]
        for result in results:
            index = results.index(result)
            results[index]=results[index].replace("\n","")
            results[index]=results[index].replace(f"{index+1}. ","")
            results[index]=float(results[index])
        plik_dane = open(f"/home/aleksander/Pulpit/python/repos/JSP2019/PYTHONFORSCIENTIST/PYTHON/SPIN{s}/DANE/daneS{s}N{n}J1H{h}.txt")
        dane = plik_dane.readlines()
        for result in dane: