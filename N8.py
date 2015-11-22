# coding: utf-8
import random


def rondo(a, b):
    return random.randrange(a, b)


class Animal:

    def __init__(self):

        self.dog_run = rondo(0, 8000)    # metrov
        self.dog_golos = rondo(0, 3000)  # golos sabaki
        self.dog_blohi = rondo(0, 100)   # sobachi vshi

        self.cow_moloko = rondo(0, 40)   # litrov moloka
        self.cow_golos = rondo(0, 450)   # cow.golos
        self.cow_run = rondo(0, 5000)    # cuw_run metrov

        self.duck_agg = rondo(0, 100)    # agg
        self.duck_golos = rondo(0, 100)  # kryua kryua
        self.duck_run = rondo(0, 100)    # run duck

    def duck_1(self):

        dk = {'agg': self.duck_agg,
              'golos': self.duck_golos,
              'run': self.duck_run}
        return dk

    def cow_1(self):

        cw = {'moloko': self.cow_moloko,
              'golos': self.cow_golos,
              'run': self.cow_run}
        return cw

    def dog_1(self):

        dg = {'blohi': self.dog_blohi,
              'golos': self.dog_golos,
              'run': self.dog_run}
        return dg
    

class Farm:

    def __init__(self):

        self.cow = rondo(1, 100)
        self.duck = rondo(1, 100)
        self.dog = rondo(1, 100)

    def status(self):

        cow = self.cow
        duck = self.duck
        dog = self.dog

        x = {'cow': cow, 'duck': duck, 'dog': dog}
        return x


class Farm_add:

    def __init__(self):

        self.cow_add = random.uniform(0.1, 2)
        self.duck_add = random.uniform(0.1, 10)
        self.dog_add = random.uniform(0.1, 1)

    def status_add(self):

        if self.cow_add > 1 or int(self.cow_add) == 2:
            cow_addd = int(self.cow_add)
        else:
            cow_addd = 0

        if self.duck_add > 1 or int(self.duck_add) == 10:
            duck_addd = int(self.duck_add)
        else:
            duck_addd = 0

        if self.dog_add > 1 or int(self.dog_add) == 1:
            dog_addd = int(self.dog_add)
        else:
            dog_addd = 0

        x_add = {'cow_add': cow_addd, 'duck_add': duck_addd, 'dog_add': dog_addd}
        return x_add


def duck_duck():

    """
    Farm
    x = {'cow': cow, 'duck': duck, 'dog': dog}
    Farm_add
    {'cow_add': cow_addd, 'duck_add': duck_addd, 'dog_add': dog_addd}
    """

    f = set()
    f = {1: Farm().status(), 2: Farm_add().status_add(), 3: Animal().duck_1()}

    return  f


def cow_cow():

    """
    Farm
    x = {'cow': cow, 'duck': duck, 'dog': dog}
    Farm_add
    {'cow_add': cow_addd, 'duck_add': duck_addd, 'dog_add': dog_addd}
    """

    f = set()
    f = {1: Farm().status(), 2: Farm_add().status_add(), 3: Animal().cow_1()}

    return  f


def dog_dog():

    """
    Farm
    x = {'cow': cow, 'duck': duck, 'dog': dog}
    Farm_add
    {'cow_add': cow_addd, 'duck_add': duck_addd, 'dog_add': dog_addd}
    """

    f = set()
    f = {1: Farm().status(), 2: Farm_add().status_add(), 3: Animal().dog_1()}

    return  f


def dc():
    print('Число уток в начале месяца - ', end='')
    col = (duck_duck()[1]['duck'])
    print(col)
    print('колличество яиц на всех уток в день - ', end='')
    col_agg = (duck_duck()[3]['agg'])
    print(col_agg)
    print('Прирост уток спустя месяц - ', end='')
    col_mes = (duck_duck()[2]['duck_add'])
    print(col_mes)
    print('Итог - ', end='')
    print('Колличество уток - ', end='')
    print(col+col_mes)
    print('Колличество яиц')


def dc():
    print('Число уток в начале месяца - ', end='')
    col = (duck_duck()[1]['duck'])
    print(col)
    print('колличество яиц на всех уток в день - ', end='')
    col_agg = (duck_duck()[3]['agg'])
    print(col_agg)
    print('Прирост уток спустя месяц - ', end='')
    col_mes = (duck_duck()[2]['duck_add'])
    print(col_mes)
    print('Итог - ', end='')
    print('Колличество уток - ', end='')
    print(col+col_mes)
    print('Колличество яиц')
    print(col_agg * 30)

def cw():

    print('Число коров в начале месяца - ', end='')
    col = (cow_cow()[1]['cow'])
    print(col)
    print('Колличество молока на всех коров в день - ', end='')
    col_mol = (cow_cow()[3]['moloko'])
    print(col_mol)
    print('Прирост коров спустя месяц - ', end='')
    col_mes = (cow_cow()[2]['cow_add'])
    print(col_mes)
    print('Итог - ', end='')
    print('Колличество коров - ', end='')
    print(col+col_mes)
    print('Колличество молока')
    print(col_mol * 30)

def dg():

    print('Число собак в начале месяца - ', end='')
    col = (dog_dog()[1]['dog'])
    print(col)
    print('Колличество блох на всех собак в день - ', end='')
    col_bloh = (dog_dog()[3]['blohi'])
    print(col_bloh)
    print('Прирост собак спустя месяц - ', end='')
    col_mes = (dog_dog()[2]['dog_add'])
    print(col_mes)
    print('Итог - ', end='')
    print('Колличество собак - ', end='')
    print(col+col_mes)
    print('Колличество блох')
    print(col_bloh * 30)
cw()
dc()
dg()
