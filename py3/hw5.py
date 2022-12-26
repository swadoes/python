n = int(input('Введите размер числа Фибоначчи '))
if n < 0: n = n*-1
f1 = f2 = 1
list1 = [f1, f2]
for i in range(2, n):
    f1,f2 = f2, f1 + f2
    list1.append(f2)
print(list1)
f1=f2=1
for i in range(-n, 1):
    f1,f2 = f2, f1 - f2
    list1.insert(0, f2)
print(list1)