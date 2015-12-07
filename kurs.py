
import os

#f = str(input('Где будем искать - '))      #   Путь откуда
#folder = str(input('Путь записи - '))      #   Путь откуда куда ( Пример I:\\[111]\\ )


f = 'D:\\[000]'                             #   Путь откуда
folder = 'D:\\[111]\\'                      #   Путь откуда куда ( Пример I:\\[111]\\ )


def fw():

    z = os.walk(f)                          #   Пробегае по дерректории считывая все содержимое

    x = []                                  #   Объевляем пустой список

    for i in z:

        b = i[0]                            #   Записываем только путь folder
        b1 = b[3:]                          #   Отсекаем корень

        x.append(b1)                        #   Записываем в список пути папок которые не будут скопированны -
                                            #   - при проходе по известным дерректориям  ' z '

        os.makedirs(folder + b1, mode=0o777, exist_ok=True)

    return x

ggg = fw()                                      #   Список чистых путей


def re():

    bob = []
    zoo = []
    goo = 0
    ltt = []
    dss = []

    for i in ggg:

        xso = i.split('\\')
        for j in xso:                           #   Список дерректорий и файлов в одном из корней
            if j not in zoo:
                zoo.append(j)

    for i in ggg:
        goo += 1

    for i in ggg:

        path_x = f[:2] + '\\' + i               #   Формерует чистый список путей для listdir
        bo = os.listdir(path_x)                 #   Временно записывает Список файлов и дерректорий в одной из папок
        bob.append(path_x)

    print(bob)
    print('''

    ''')

    for i in bob:
        ltt = os.listdir(i)
        for j in ltt:
            ds = [i + '\\' + j]
            dss.append(ds)                      #   Создатель общего списка файлов при сопостовлении со списком
                                                #   - bob. Имена из bob пропускаются
    print('''
    ''')
    print(dss)

# -----------   dss Список создания
# -----------   bob Список пропуска




re()
