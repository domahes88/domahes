#Делаем программу "students_list.py ".2222

#1. Она должна сделать следующее:
#Создаем список.
#Заполняем его нашими именами (+фамилиями).                                     +
#2. Выводим имя одного студента на экран:                                       +
#Получаем индекс через функцию input().                                         +
#Выводим на экран студента по этому индексу.                                    +
#3. Выводим на экран имена нескольких студентов:                                +
#Получаем через input() начало и конец среза.                                   ++
#Выводим на экран студентов из такого среза.                                    +
#4. Находим количество студентов, в именах которых есть буква "р".              +
#5. Находим группы студентов с одинаковыми именами и создаем списки этих групп.

stud = {1:'Kuklus Kipelov', 2:'kudryajka Siyu', 3:'Ahmed Lujin', 4:'Dmitriy Dimidov',
        5:'Chert Vplatiy', 6:'Kuklus Klan', 7:'Dmitriy Kozlov', 8:'Ahmed Mazur',
        9:'Portnoiy Pan'}

v = int(input('V nashem mnojestve ' + str(len(stud)) +
          ' ctudentov. kogo iz nih vivesti? '))
print(stud[v])
a = int(input('podgotovim srez 1 e cheslo - '))
b = int(input('podgotovim srez 2 e cheslo - '))
for i in range(a, b + 1):
    print(stud[i])
#Poisk 'p, P' kollichestvo studentov
q = 0
for i in stud:
    for j in stud[i]:
        if j == 'p' or j == 'P':
            q += 1
            break
print(q, '<<< kollichestvo studentov s P, p')
st = []
gp = []
for j in stud:
    st.append(stud[j])
for t in st:
    for r in stud:
        if stud[r].split()[0] == t.split()[0]:
            if stud[r] not in gp:
                gp.append(stud[r])
print(gp)
