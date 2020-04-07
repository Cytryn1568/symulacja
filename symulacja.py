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
        status (str): status ze zbioru 'zdrowy', 'chory', 'nosiciel', 'wyleczony'
        tura: ilosc tur przez ktore byl chory
    
    """
    
    def __init__(self, x=0, y=0, status = 'zdrowy', tura = 0):
        self.x = x
        self.y = y
        self.set_status(status)
        self.tura = tura
            
    def get_status(self):
        return self.set_status
    
    def set_status(self,wartosc):
        """ uzytkownik programu moze nadac pacjentowi tylko status z listy """
        if wartosc not in ['zdrowy', 'chory', 'nosiciel', 'wyleczony']:
            raise ValueError("Nie ma takiego statusu")
        self.status = wartosc
            
            
    def ruch(self):
        """Wykonaj ruch zmieniając współrzędne x,y.
        
        Zdrowy pacjent przesuwa się o 0-1, a chory o 0-0.1"""
        if self.status == 'chory':
            zasieg = 0.1
        else:
            zasieg = 1
        self.x = self.x + random.uniform(-zasieg, zasieg)
        self.y = self.y + random.uniform(-zasieg, zasieg)
        if self.status == 'chory':
            self.tura = self.tura + 1
        
        
    def __str__(self):
        return "Pacjent " + self.status + " @ "  + str(self.x) + " x " + str(self.y) + " @ " + str(self.tura)
    

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
            zdrowy = random.choices( ['zdrowy', 'chory'], [80, 20] )[0]
            self._pacjenci.append( Pacjent(x, y, zdrowy) )
    
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
            self.wyzdrowienia()
    
    def zaraza(self):
        """ sprawdz czy blisko pacjenta nie ma chorego i zaraz go 
        z odpowienim prawdopodobienstwem"""
        for p in self._pacjenci:
            if p.status == 'zdrowy':
                for p2 in self._pacjenci:
                    zarazi = random.choices( [True, False], [50, 50] )[0]
                    dystans = sqrt( (p.x - p2.x)**2 + (p.y - p2.y)**2 )
                    if dystans>0 and dystans<20 and p2.status == 'chory' and zarazi:
                        p.status = 'chory'
                        break
                    
    def wyzdrowienia(self):
        """ kto byl chory x tur wyzdrowieje """
        for p in self._pacjenci:
            if p.tura >= 10 and p.status == 'chory':
                p.status = 'wyleczony'
    
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
