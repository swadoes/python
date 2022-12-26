x = [2, 3, 5, 9, 3]

summ = 0
for i in range(1, len(x), 2):
        summ += x[i]       
print(f"{x} -> сумма элементов на нечётных позициях: {summ}")
