# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# def array():
#     element = int(input("--> "))
#     list_number = []
#     for i in range(element):
#         list_number = random.sample(range(15), element)
#     return list_number    



# result = []
# list_number = [1,2,3,4,5]
# for i in range(int(len(list_number) / 2)):
#         first = (list_number[i])
#         for j in range(int(len(list_number) / 2)):
#             last = (list_number[-1-i])
#             result = first * last
#         print(result)

from math import ceil
import random
from unittest import result

def RAN():
    N = int(input('Введите длину списка: '))
    lst = []
    for i in range(N):
        lst.append(random.randint(-N, N))
    return lst


def OLL(list_number):
    result = []
    for i in range(int(ceil(len(list_number) / 2))):
        result.append(list_number[i] * list_number[-1-i])
    return result

num_1 = RAN()
res = OLL(num_1)  
print(num_1)
print(res)

