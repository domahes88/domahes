import os

"""
"""
def copy_dir():

    x = 0
    f_walk = os.walk(input('Входная папка - '))
    for i in f_walk:

        x += 1
    print(x-1)
"""
"""
('D:/000222', 'D:/[000]/www')
"""



def fw():

    f = str(input('Где будем искать - '))
    way = str(input('Путь записи - '))
    z = os.walk(f)
    x = 0

    for i in z:

        print(i[0])

        """
        ld = os.listdir(i[0])                                           #Создании библтотеки                                ld = библиотека
        for g in ld:
            print(g)

        """

        """
        for t in ld:
            print(t)
            print('____________')
            os.makedirs()
        """


        #mld = str(ld).replace(f, way)                                   #Модефецированный путь                              ld = библиотека
        #print(mld)


        #os.makedirs(mld, mode=0o777, exist_ok=True)



        x += 1
        if x == 3:
            pass

    #os.symlink(z, 'D:/[111]/000' + '33', target_is_directory=False)

fw()
"""
__________________________________________________________________________________________________________________________
import os


def fw():

    f = str(input('Где будем искать - '))   #   Путь откуда
    folder = str(input('Путь записи - '))   #   Путь откуда куда ( Пример I:\\[111]\\ )

    z = os.walk(f)                          #   Пробегае по дерректории считывая все содержимое

    x = []                                  #   Объевляем пустой список



    for i in z:

        b = i[0]                            #   Записываем только путь folder
        b1 = b[3:]                          #   Отсекаем корень
        print(b1)

        x.append(b1)                        #   Записываем в список пути папок которые не будут скопированны -
                                            #   - при проходе по известным дерректориям  ' z '

        os.makedirs(folder + b1, mode=0o777, exist_ok=True)
        #os.symli


fw()
