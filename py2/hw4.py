from random import Random, randint


N = int(input('Введите число'))
numbers = []
for i in range(N):
    numbers.append(randint(-N,N+1))
    
print(numbers)
print(numbers[1] * numbers[3])

f = open('file.txt', 'w')
while True:
    s = input('Укажите позицию для вычисления - ')
    if s == "":
        break
    f.write(s+"\n")
f.close()

result = 1
f = open('file.txt', 'r')
for line in f:
    if line == "":
        break
    result *= numbers[int(line)]
f.close()
print(result)