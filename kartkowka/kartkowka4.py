#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
lista_1=[20,11,[5,-8],[1,-20],5,[-19,-8],-10,[7,-19],-15,[6,-12],[-17,9],2]
lista_2 =[-1,-3,7,9,[0,2],[2,4],[-1,0]]
def zadanie(lista):
	def compare(x):
		return abs(x[0])
	listahelp1 = []
	listahelp2 = []
	for x in range(0,len(lista)):
		y = lista[x]
		if type(y)==int:
			listahelp1.append(y)
	print(listahelp1)
	for x in range(0,len(lista)):
		y = lista[x]
		if type(y)==list:
			listahelp2.append(y)
	print(listahelp2)
	listahelp2=sorted(listahelp2, key=compare)
	listahelp1=sorted(listahelp1,key=abs)
	lista_1=listahelp1+listahelp2
	print(lista_1)
	return lista_1
zadanie(lista_1)
zadanie(lista_2)

