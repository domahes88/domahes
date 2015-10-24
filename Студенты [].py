# Kharchenko
stud = ['Gorimika Zlodeev', 'Klimontii Suhomykishev', 'koshey Kvyat P', 'Babrich Loskutov', 'Klimontii Suhomykishev', 'Lesorub Ejov', 'Patrik kolomin']
nf = stud[0].split(' ') # Конструкция припер по разбитию Имя и фомилии по элименту пробела
print('Всего в нашем замечательном списке студентов ' + str(len(stud)) + ' человека')
#print(nf[0])
w = 1
w1 = input('Хотите выбрать из 4-х, y или n --- ')
print()
print()
if w1 == 'y':
    w = int(input('от 1 - о до 4 - х --- ')) - 1
else:
    print('Тогда я выберу сам из одного заранее подготовленного имени!')
print()
print()
#*****************
x = 0
print('Давайте получим  индекс студента ---', stud[w])
d = input('Вы согластны? y или n ? --- ')
if d == 'y':
    for i in stud:
        x += 1
        if i == str(stud[w]):
            print('он ' + str(x) + '-й')
            break
else:
    print('Ну тогда съешь ежа', '\n', '''И да find не ищет по полному имени в списке''')
    
if d == 'y':
    print()
    print()
    print()
    print()
    d = int(input('Если ты уверен в своих силах потрудись вспомнить каким числом едет ' + str(stud[w]) + ' и нажми соответствующую кнопку --- '))
    if d - 1 == w:
        print('Это правельный ответ')
    else:
        print('Это неправельный ответ - Съешь бобра')
else:
    pass
print()
srez1 = int(input('nu teperi srez ot 0 do 4 vvodi 1e chislo sreza --- '))
srez2 = int(input('nu teperi srez ot 0 do 4 vvodi 2e chislo sreza --- '))
vivod = stud[srez1:srez2]
#if (srez1 == True) and (srez2 == True):
#    print(vivod)
#else:
#    print('siesh Morja')
print(vivod)
print()
cheslo = 0
cheslo1 = 0
for k in stud:
    #print(k)
    for j in k:
        if j == 'p' or j == 'P':
            cheslo += 1
print('Более того теперь нам известно сколько у нас -P- ' + str(cheslo) + ' ура товарищи')
h1 = 0
#for j in stud[h1:]:
#    pass
#    for h in range(len(stud)+1):
#        if j == stud[h1+1]
    
#print('Ктомуже унаяс есть повторы ' + str(cheslo1))
