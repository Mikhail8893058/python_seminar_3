# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
#              0  1  2  3  4
list_number = [1, 2, 3, 4, 5, 12, 43, 23]
summ = 0

for i in range(1, len(list_number), 2):
        summ += int(list_number[i])
        print(i)
        print(int(list_number[i]))
print('Сумма элементов списка, стоящих на нечетной позиции:=',summ)    

# for i in range(1, len(list_number)):
#     if int(i) % 2 == 1:
#         print(i)
#         summ += int(list_number[i])
#         print('Сумма элементов списка, стоящих на нечетной позиции:=',summ)    
