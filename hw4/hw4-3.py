# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

import random
listt = [random.randint(0,10) for i in range (10)]
print(listt)
listt1 =[]
[listt1.append(i) for i in listt if i not in listt1 ]
print(listt1)