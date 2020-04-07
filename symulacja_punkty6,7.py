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
            v_x = random.uniform(-0.1, 0.1)
            v_y = random.uniform(-sqrt(0.01 - v_x**2), sqrt(0.01 - v_x**2))
            self._pacjenci.append( Pacjent(x, y, v_x, v_y, zdrowy) )
    
