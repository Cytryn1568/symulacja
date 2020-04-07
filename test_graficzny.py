# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:22:54 2020

@author: User
"""


import matplotlib
matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#from symulacja import Populacja #cos nie tak
import symulacja

pop = Populacja(20)

fig, ax = plt.subplots()

wykresy = { 'zdrowy' : plt.plot([],[],'go')[0],
           'chory' : plt.plot([],[],'ro')[0],
           'nosiciel' : plt.plot([],[],'yo')[0],
           'wyleczony' : plt.plot([],[],'bo')[0],
           }
#ln, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(0, pop.szerokosc)
    ax.set_ylim(0, pop.wysokosc)
    return wykresy.values()

def update(frame):
    pop.ruch()
    for status,wykres in wykresy.items():
        xdata = [p.x for p in pop._pacjenci if p.status == status]
        ydata = [p.y for p in pop._pacjenci if p.status == status]
        wykres.set_data(xdata,ydata)
    return wykresy.values()

ani = FuncAnimation(fig, update, frames=None,
                     init_func=init, blit=True)
plt.show(block=True)
