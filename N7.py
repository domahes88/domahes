class Tank:

    def __init__(self):
        
        self.model = input('Это модель танка - ')

        self.shasi = []
        while self.shasi != 'y':
            self.shasi = input('Шасси танка y/n - ')
            if self.shasi == 'n':
                break
        if self.shasi == 'y':
                self.shasi = 'Устоновленно!'
        else:
            self.gusinici = 'Не устоновленно!'


        self.gusinici = []
        while self.gusinici != 'y':
            self.gusinici = input('Гусиници танка y/n - ')
            if self.gusinici == 'n':
                break
        if self.gusinici == 'y':
                self.gusinici = 'Устоновленно!'
        else:
            self.gusinici = 'Не устоновленно!'


        self.skorosti = input('Скорость танка - ')
        if self.shasi != 'Устоновленно!' or self.gusinici != 'Устоновленно!':
            self.skorosti = 0


    def status(self):
        print('Модель танка: {}, Шасси танка: {}, Гусиници танка: {}, Скорость танка: {}'.format(self.model, self.shasi, self.gusinici, self.skorosti))

    def change(self):
        
        g = input('Снять шасси танка? - y/n - ')
        if g == 'y':
            self.colesa = 'Не устоновленно!'
            self.skorosti = 0
        else:
            pass
        
        d = input('Снять гусиници танка? - y/n - ')
        if d == 'y':
            self.colesa = 'Не устоновленно!'
            self.skorosti = 0
        else:
            pass

class Car:
    
    def __init__(self):
        
        self.model = input('Это модель машины - ')

        self.colesa = []
        while self.colesa != 'y':
            self.colesa = input('Колеса машины y/n - ')
            if self.colesa == 'n':
                break
        if self.colesa == 'y':
            self.colesa = 'Устоновленно!'
        else:
            self.colesa = 'Не устоновленно!'
           
        self.skorosti = input('Скорость машины - ')
        if self.colesa != 'Устоновленно!':
            self.skorosti = 0

    def status(self):
        
        print('Это модель машины: {}, Колеса машины: {}, Скорость машины: {}'.format(self.model, self.colesa, self.skorosti))

    def change(self):
        
        g = input('Снять колеса с машины? - y/n - ')
        if g == 'y':
            self.colesa = 'Не устоновленно!'
            self.skorosti = 0
        else:
            pass



class Telega:

    def __init__(self):
       
        self.colesa = []
        while self.colesa != 'y':
            self.colesa = input('Колеса телеги y/n - ')
            if self.colesa == 'n':
                break
        if self.colesa == 'y':
            self.colesa = 'Устоновленно!'
        else:
            self.colesa = 'Не устоновленно!'
          
        self.skorosti = input('Скорость телеги - ')
        if self.colesa != 'Устоновленно!':
            self.skorosti = 0

    def status(self):
        
        print('Колеса телеги: {}, Скорость телеги: {}'.format(self.colesa, self.skorosti))

    def change(self):
        
        g = input('Снять колеса с телеги? - y/n - ')
        if g == 'y':
            self.colesa = 'Не устоновленно!'
            self.skorosti = 0
        else:
            pass


def list_list():
    
    t, c, tg = Tank(), Car(), Telega()
    cars = [t, c, tg]
    print()
    [i.status() for i in cars]
    print()
    g = input('Жилаете внести изминения? - y/n - ')
    if g == 'y':
        t.change()
        c.change()
        tg.change()
    else:
        pass
    print()
    [i.status() for i in cars]


def pusk():
    
    g = input('Жилаете начать ввод? - y/n - ')
    if g == 'y':
        list_list()
    else:
        print('подумайте еще раз - !', '\n')
        pusk()
pusk()
