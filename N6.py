
import os

global x
x = []

def ld():
    
    print('укажите где будем искать!')
    open_hard = input('диск - ')
    open_folder = input('папка - ')
    open_dir = open_hard + ':/' + open_folder
    x.append(open_dir)#запись пути в глобальную переменную
    return open_dir

def find():

    try:
        f = os.listdir(ld())
        return f
        
    except FileNotFoundError:
        print('Такого пути нет? попробуйте еще раз!')
        open_folder()

def grep():
    print('укажите тип файла в котором будет идти поиск - ')
    w = input('Это могут быть txt или py ... или что то еще - ')

    for e, i in enumerate(find()):
        if str('.') + w in i:
            yield e, i
def fg():
    pin = input('укажите что будем искать - ')
    for e, i in grep():
        f = open(x[0] + '/' + i).read()
        if f.count(pin):
            print('________________________________________________')
            print(i, '\n')
            for j in f:                
                print(j, end='')
            #Выдает через yield имя файла, номер строки и строку.
        

def poisk():
    f = input('Жилаете ли вы осуществить поис по пораметрам? yes или no - ')
    if f == 'yes':
        for e, i in grep():
            print(e, i)
    else:
        print('порой решение доется не сразу')
        poisk()

#N1

def proverca():
    n = input("""Жилаете проверить 1 или 2-е задание?
Ведите соответствующую цифру - """)
    if n == '1':
        print('---------')
        poisk()
    elif n == '2':
        print('---------')
        fg()
    else:
        print('И все же....!')
        proverca()
proverca()
