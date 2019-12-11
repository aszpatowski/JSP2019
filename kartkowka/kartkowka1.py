#!/usr/bin/python3.6
def zadanie1():
	a = int(input("Podaj liczbe: "))
	b = int(input("Podaj liczbe: "))
	c = a%b
	print("Reszta z dzielenia to: ", c)
def zadanie2():
	import math
	import numpy as np
	a = float(input("Podaj pierwszy bok: "))
	b = float(input("Podaj drugi bok: "))
	c = float(input("Podaj trzeci(najdluzszy) bok: "))
	x = a**2+b**2-c**2
	cosin = x/(2*a*b)
	rad= np.arccos(cosin)
	angle = math.degrees(rad)
	print(cosin)
	print(rad)
	print("Kąt to: ",angle)
zadanie2()

