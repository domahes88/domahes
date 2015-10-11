# domahes
import os
t = 0
f = os.listdir('I:/002')
#print(f)
for i in f:
    h = open(i).read()          #Чтение документов по отдельности
    if h.count('python'):       #Если в h(в документе) есть строка с python
        t += 1                  # +1 документ содержит строку
print(t, ' -Документов включают "python" c учетом сценнария')
