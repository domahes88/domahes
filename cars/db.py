import pickle

def creat_list():

    d = []
    global x
    name = input('Введите имя файла - ')
    if d != open('d:/' + str(name), 'wb'):
        d = open('d:/' + str(name), 'wb')
        x = d

    else:
        pass

def zapis():

    car     =   input('Введите авто - ')
    nomer   =   input('Государственный знак - ')
    ls      =   input('Мощность - ')

    t = []
    t.append([car, nomer, ls])

    y = input('Желаете завершить ввод? если да то введите stop - ')

    if y == 'stop':
        pickle.dump(t, x)
        x.close()

    else:
        zapis()

def mem():
    a = x.name
    return a
