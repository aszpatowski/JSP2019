#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import numpy as np
def zadanie1():
    A = np.array([[1,2,3,-2,-1],[3,5,5,-3,-9],[2,3,2,0,-8],[2,6,7,-5,1],[1,2,6,-4,-10]])
    B = np.array([6,2,-5,17,12])
    answers = np.linalg.solve(A,B)
    print("x =",answers[0],"\ny =",answers[1],"\nz =",answers[2],"\nt =",answers[3],"\nu =",answers[4])
zadanie1()


