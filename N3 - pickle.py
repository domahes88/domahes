"""
»> import pickle000
»> data = {
... 'a': [1, 2.0, 3, 4+6j],
... 'b': ("character string", b"byte string"),
... 'c': {None, True, False}
... }
»>
»> f = open('c:/temp/data.pickle', 'wb')
... pickle.dump(data, f)
...
»> with open('data.pickle', 'rb') as f:
... data_new = pickle.load(f)
1. Сделайте простую базу данных:
Пользователь вводит команду: ввести, вывести
- Ввести - пользователь вводит марку автомобиля и его мощность.
Необходимо проверить, что марка состоит только из букв
латинского или русского алфавитов. Мощность только из цифр.
- Вывести - выводятся все автомобили - по алфавиту.
Сортировку сделать сначала стандартным методом.
Затем написать свою версию сортировки циклами.
2. Реализовать поиск/фильтрацию в базе данных - то есть вывод по условию.
- По мощности - конкретное число, больше, меньше, в промежутке.
- По вхождению слова в название.
- По полному соответствию слова.

"""
import pickle

#1

n, f, model, ls = 1, [], [], []

while f != 'stop':
    model.append(input(str(n) + ' модель авто - '))       
    ls.append(input('лошадиные силы - '))
    n += 1
    f = input('''
Ведите stop, если продолжит нажмите enter ''')

f = open('c:/temp/rino', 'wb')
    
model_s = []
for i in range(len(model)): #Создаем единый список авто + мощность "[[a, 1], [b, 2], ...]]"
    model_s.append([model[i]])
    model_s[i].append(ls[i])

#запись в pycle

pickle.dump(model_s, f)
f.close()

#проверка на буквы и цифры

for j in range(len(model_s)):
    if str(model_s[j][0]).isalpha():
        pass
    else:
        print('строка ' + str(model_s[j][0]) + ' не состаит только из букв')
    if str(model_s[j][1]).isdigit():
        pass
    else:
        print('строка ' + str(model_s[j][1]) + ' не состаит только из цифр')

#Сортировка по алфовиту
epa = model
epa.sort()

print("""
сортировка

""")

for i in epa:
    print(i)

#Своя сортировка циклами из файла

f = open('c:/temp/rino', 'rb')
read = pickle.load(f)
print(read)
