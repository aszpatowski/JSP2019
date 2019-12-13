#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
def rzut(v0,angle):
     sinalfa = np.sin(np.deg2rad(angle))
     cosalfa = np.cos(np.deg2rad(angle))
     g = 9.81
     v0x =   v0* cosalfa
     v0y = v0* sinalfa
     Hmax = v0y*v0y/(2*g)
     Range =(2*(v0*v0)*sinalfa*cosalfa)/g
     tfly = (2*v0y)/g
     print(Hmax,"metrów", Range, tfly)
     t= np.linspace(0,tfly, num=10)
     vx = np.ones(10)*v0x
     vy = np.ones(10)*v0y-(g*t)
     y = v0y*t - (g/2)*(t**2)
     x = v0x*t
     print(t)
     print(vx)
     print(vy)
     plt.subplot(3,1,1)
     plt.plot(t,vx,label="VX")
     plt.plot(t,vy,label="VY")
     plt.ylabel('v [m/s]')
     plt.xlabel('t [s]')
     plt.legend(loc="lower left")
     plt.subplot(3, 1, 2)
     plt.plot(t,y)
     plt.ylabel('y [m]')
     plt.xlabel('t [s]')
     plt.subplot(3, 1, 3)
     plt.plot(x,y)
     plt.ylabel('y [m]')
     plt.xlabel('x [m]')
     plt.show()
rzut(10,45)