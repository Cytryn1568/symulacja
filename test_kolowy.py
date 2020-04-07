# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 11:04:36 2020
Rysujemy nie tylko poruszających się pacjentów, lecz także wykres kołowy ich statusu.
@author: magda
"""

import matplotlib
matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from symulacja import Populacja

pop = Populacja(20, 50, 50)

fig, (ax1, ax2) = plt.subplots(1, 2)

wykresy = { 'zdrowy' : ax1.plot([],[],'go')[0],
           'chory' : ax1.plot([],[],'ro')[0],
           'nosiciel' : ax1.plot([],[],'yo')[0],
           }

kolo = plt.pie([], labels=[], autopct='%1.1f%%',
        shadow=True, startangle=90)
kolo_dane = {'zdrowy': 0, 'chory': 0, 'nosiciel': 0}

def init():
    ax1.set_xlim(0, pop.szerokosc)
    ax1.set_ylim(0, pop.wysokosc)
    return wykresy.values(), kolo

def update(frame):
    pop.ruch()
    #szykujemy poruszające się kropki
    for status,wykres in wykresy.items():
        xdata = [p.x for p in pop._pacjenci if p.status == status]
        ydata = [p.y for p in pop._pacjenci if p.status == status]
        wykres.set_data(xdata, ydata)  
    #szykujemy wykres kolowy
    ax2.clear()
    kolo_dane['zdrowy']=0
    kolo_dane['chory']=0
    kolo_dane['nosiciel']=0
    for p in pop._pacjenci:
        if p.status == 'zdrowy':
            kolo_dane['zdrowy']+=1
        elif p.status == 'chory':
            kolo_dane['chory']+=1
        else:
            kolo_dane['nosiciel']+=1
    for status,liczba in kolo_dane.items():
        liczba=liczba*100/len(pop._pacjenci)
    kolo = plt.pie(kolo_dane.values(), labels=kolo_dane.keys(), colors=['g', 'r', 'y'],
                   autopct='%1.1f%%', shadow=True, startangle=90)
    return wykresy.values(), kolo

ani = FuncAnimation(fig, update, frames=None,
                    init_func=init, blit=False)

plt.show(block=True)