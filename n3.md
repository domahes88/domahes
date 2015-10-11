# domahes
a = [1, -20, 38, 0, 44]
b = [88, -20, 48, 4, 33, 2]
if len(a) > len(b):
    x = a
else:
    x = b
x1 = int(len(x))
x0 = []
for i in x1:
    if a[i-1] < b[i-1]:
        x0.add(a[i-1])
    if a[i-1] > b[i-1]:
        x0.add(b[i-1])
print(x0)
