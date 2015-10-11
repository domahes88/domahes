# domahes
import os
t = 0
name = []
f = os.listdir('I:/002')
#print(f)
for i in f:
    h = open(i).read()          #Чтение документов по отдельности
    if h.count('python'):       #Если в h(в документе) есть строка с python
        t += 1                  # +1 документ содержит строку
        name.append(i)
        name.append('\n')
for p in name:
    print(p, '\n')
print(t, ' - Документов включают "python" c учетом сценнария')

file = open('I:/002/result.txt', 'w')
for u in name:
    file.write(u)
t1 = '-----'
file.write(t1)
file.write(str(int(t-1)))
file.close()    
