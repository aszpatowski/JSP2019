#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
def rzut(v0,angle):
     N = 15
     sinalfa = np.sin(np.deg2rad(angle))
     cosalfa = np.cos(np.deg2rad(angle))
     g = 9.81
     v0x =   v0* cosalfa
     v0y = v0* sinalfa
     Hmax = v0y*v0y/(2*g)
     Range =(2*(v0*v0)*sinalfa*cosalfa)/g
     tfly = (2*v0y)/g

     print("Maksymalna wysokość:",Hmax,"metrów.","\nZasięg rzutu:",Range,"metrów.","\nCzas lotu: ", tfly,"sekund.")
     t= np.linspace(0,tfly, num=N)
     vx = np.ones(N)*v0x
     vy = np.ones(N)*v0y-(g*t)
     y = v0y*t - (g/2)*(t**2)
     x = v0x*t
     r = np.sqrt(x**2+y**2)
     plt.subplot(3,1,1)
     plt.plot(t,vx,label="VX")
     plt.plot(t,vy,label="VY")
     plt.ylabel('v [m/s]')
     plt.xlabel('t [s]')
     plt.legend(loc="lower left")
     plt.subplot(3, 1, 2)
     plt.plot(t,x, label="X(t)")
     plt.ylabel('x [m]')
     plt.xlabel('t [s]')
     plt.legend(loc="upper left")
     plt.twinx()
     plt.plot(t,y,color="red", label="Y(t)")
     plt.legend(loc="center left")
     plt.ylabel('y [m]')
     plt.xlabel('t [s]')
     plt.subplot(3, 1, 3)
     plt.plot(x,y)
     plt.ylabel('y [m]')
     plt.xlabel('x [m]')
     plt.show()
     return
rzut(10,45)