# coding: utf-8
def start():
        return input()


class Tank:

    def __init__(self):
        print('Это модель такнка - ', end='')
        self.model = start()

        self.shasi = []
        while self.shasi != 'y':
            print('Шасси танка y/n - ', end='')
            self.shasi = start()
            if self.shasi == 'n':
                break
        if self.shasi == 'y':
                self.shasi = 'Устоновленно!'
        else:
            self.gusinici = 'Не устоновленно!'


        self.gusinici = []
        while self.gusinici != 'y':
            print('Гусиници танка y/n - ', end='')
            self.gusinici = start()
            if self.gusinici == 'n':
                break
        if self.gusinici == 'y':
                self.gusinici = 'Устоновленно!'
        else:
            self.gusinici = 'Не устоновленно!'

        print('Скорость танка - ', end='')
        self.skorosti = start()
        if self.shasi != 'Устоновленно!' or self.gusinici != 'Устоновленно!':
            self.skorosti = 0


    def status(self):
        print('Модель танка: {}, Шасси танка: {}, Гусиници танка: {}, Скорость танка: {}'.format(self.model, self.shasi, self.gusinici, self.skorosti))

    def change(self):

        print('Снять шасси танка? - y/n - ', end='')
        g = start()
        if g == 'y':
            self.shasi = 'Не устоновленно!'
            self.skorosti = 0
        else:
            pass
        print('Снять гусиници танка? - y/n - ', end='')
        d = start()
        if d == 'y':
            self.gusinici = 'Не устоновленно!'
            self.skorosti = 0
        else:
            pass

class Car:
    
    def __init__(self):
        print('Это модель машины - ', end='')
        self.model = start()

        self.colesa = []
        while self.colesa != 'y':
            print('Колеса машины y/n - ', end='')
            self.colesa = start()
            if self.colesa == 'n':
                break
        if self.colesa == 'y':
            self.colesa = 'Устоновленно!'
        else:
            self.colesa = 'Не устоновленно!'
        print('Скорость машины - ', end='')
        self.skorosti = start()
        if self.colesa != 'Устоновленно!':
            self.skorosti = 0

    def status(self):
        
        print('Это модель машины: {}, Колеса машины: {}, Скорость машины: {}'.format(self.model, self.colesa, self.skorosti))

    def change(self):
        print('Снять колеса с машины? - y/n - ', end='')
        g = start()
        if g == 'y':
            self.colesa = 'Не устоновленно!'
            self.skorosti = 0
        else:
            pass

class Telega:

    def __init__(self):
       
        self.colesa = []
        while self.colesa != 'y':
            print('Колеса телеги y/n - ', end='')
            self.colesa = start()
            if self.colesa == 'n':
                break
        if self.colesa == 'y':
            self.colesa = 'Устоновленно!'
        else:
            self.colesa = 'Не устоновленно!'
        print('Скорость телеги - ', end='')
        self.skorosti = start()
        if self.colesa != 'Устоновленно!':
            self.skorosti = 0

    def status(self):
        
        print('Колеса телеги: {}, Скорость телеги: {}'.format(self.colesa, self.skorosti))

    def change(self):
        print('Снять колеса с телеги? - y/n - ', end='')
        g = start()
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

