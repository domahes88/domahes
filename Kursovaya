
import os


#f = str(input('Где будем искать - '))      #   Путь откуда
#folder = str(input('Путь записи - '))      #   Путь откуда куда ( Пример I:\\[111]\\ )


f = 'D:\\lib'                             #   Путь откуда
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
    zzz = []

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
    print('_________________________________________________________________________________________')

    for i in bob:
        ltt = os.listdir(i)
        for j in ltt:
            ds = [i + '\\' + j]
            dss.append(ds)                      #   Создатель общего списка файлов при сопостовлении со списком
                                                #   - bob. Имена из bob пропускаются
    #print(dss)
    print('''
    ''')

    rob = []
    for j in dss:
        rob.append(j[0])

    print(rob)
    print('''
    robrobrobrobrobrobrobrobrobrob
    ''')
    r = []
    for i in rob:
        r.append(i)

    print(r)
    print('______________________________________________________')




# -----------   rob Список создания
# -----------   bob Список пропуска

    for i in rob:

        x = str(folder[:2])
        x1 = i[2:]
        x2 = x + x1
        print(x2)
        zzz.append(x2)

    print(zzz)

    for i in zzz:
        x = str(folder)
        if i not in bob:
            g = i[3:]
            g1 = x + g
            print(g1)
            os.symlink(i, g1)



# -----------   zzz Список создания
# -----------   bob Список пропуска


print('ok')




re()
