# -*- coding: utf-8 -*-
"""Program do symulacji rozprzestrzeniania choroby w populacji
Kod do wykorzystania na zajęciach 01.04.2020
"""

import random
from math import sqrt

class Pacjent:
    """Pojedyncza osoba w symulacji. 
    
    Atrybuty:
        x (float): współrzędna x pozycji Pacjenta
        y (float): współrzędna y pozycji Pacjenta
        v_x (float): prędkość Pacjenta w kierunku x
        v_y (float): prędkość Pacjenta w kierunku y
        status (str): status ze zbioru 'zdrowy', 'chory', 'nosiciel'"""
    
    def __init__(self, x=0, y=0, v_x = 0, v_y = 0, czy_zdrowy=True):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        if czy_zdrowy:
            self.status = 'zdrowy'
        else:
            self.status = 'chory'
            
            
    def ruch(self):
        """Wykonaj ruch zmieniając współrzędne x,y.
        Zdrowy pacjent przesuwa się z prędkością  
        z zakresu z 0-1 i przyspieszeniem z 0-0.1, a chory z prędkością z 0-0.1 
        i przyspieszeniem z 0-0.01."""
      
        if self.status == 'chory':
            predkosc_max = 0.1
        else:
            predkosc_max = 1
        zmiana_v_x = random.uniform(-predkosc_max/10, predkosc_max/10)
        zmiana_v_y = random.uniform(-predkosc_max/10, predkosc_max/10)
        if (self.v_x + zmiana_v_x)**2 + (self.v_y + zmiana_v_y)**2 > predkosc_max**2:
            self.v_x = self.v_x
            self.v_y = self.v_y
        else:
            self.v_x = self.v_x + zmiana_v_x 
            self.v_y = self.v_y + zmiana_v_y
        self.x = self.x + self.v_x
        self.y = self.y + self.v_y
        
        
    def __str__(self):
        return "Pacjent " + self.status + " @ "  + str(self.x) + " x " + str(self.y)
    

class Populacja:
    """Zbiór Pacjentów w ograniczonym obszarze przestrzeni
    
    Atrybuty:
        szerokosc (float): szerokosć dostępnego obszaru
        wysokosc (float): wysokosć dostępnego obszaru
        
    """
        
    def __init__(self, n, wysokosc=100, szerokosc=100):
        """Tworzy populację n Pacjentów na danym obszarze.
        
        Argumenty:
            n (int): liczba pacjentów
            wysokosc (float, optional): wysokosć planszy
            szerokosc (float, optional): szerokosć planszy            
        """
        self._pacjenci = []
        self.wysokosc = wysokosc
        self.szerokosc = szerokosc
        
        for i in range(n):
            x = random.uniform(0, szerokosc)
            y = random.uniform(0, wysokosc)
            
            zdrowy = random.choices( [True, False], [80, 20] )[0]
            self._pacjenci.append( Pacjent(x, y, zdrowy) )
            if self.status == 'chory':
                predkosc_max = 0.1
            else:
                predkosc_max = 1
            v_x = random.uniform(-predkosc_max, predkosc_max)
            v_y = random.uniform(-sqrt(predkosc_max**2 - v_x**2), sqrt(predkosc_max**2 - v_x**2))
            self._pacjenci.append( Pacjent(x, y, v_x, v_y, zdrowy) )
    def __str__(self):
        s = ""
        for p in self._pacjenci:
            s += str(p) + "\n"
        return s
    
    def ruch(self):
        """ Wykonaj ruch przesuwając każdego z pacjentów"""
        for p in self._pacjenci:
            p.ruch()
            p.x = p.x % self.szerokosc
            p.y = p.y % self.wysokosc
            self.zaraza()
    
    def zaraza(self):
        """ sprawdz czy blisko pacjenta nie ma chorego i zaraz go 
        z odpowienim prawdopodobienstwem"""
        for p in self._pacjenci:
            if p.status == 'zdrowy':
                for p2 in self._pacjenci:
                    zarazi = random.choices( [True, False], [1, 99] )[0]
                    dystans = sqrt( (p.x - p2.x)**2 + (p.y - p2.y)**2 )
                    if dystans>0 and dystans<5 and p2.status == 'chory' and zarazi:
                        p.status = 'chory'
                        break
    
    def zmiana_wymiarow(self, wysokosc, szerokosc):
        """ Podaj nową wysokosc i szerokosc szpitala - zmienimy jego wymiary.
        Jesli którys z pacjentów znajduje się poza jego granicami,
        sprowadzimy go na granicę."""
        for p in self._pacjenci:
            if p.x>szerokosc:
                p.x=float(szerokosc)
            if p.y>wysokosc:
                p.y=float(wysokosc)
        self.wysokosc=wysokosc
        self.szerokosc=szerokosc
    
    def zapisz(self,nazwa_pliku):
        fout = open(nazwa_pliku,'w')
        fout.write(str(self))
        fout.close()