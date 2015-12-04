import os

def copy():

    walk = os.listdir('D:/')

    for i in walk:
        os.makedirs('D:/[000]/' + i, mode=0o777, exist_ok=True)       #КОПИРУЕТ ДЕРРИКТОРИИ


def copyw():



    s = os.walk(input('дерректория - '))

    for i in s:
        print(i)





copyw()

os.
