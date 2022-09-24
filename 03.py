import random
# def array():
#     element = int(input("--> "))
#     list_number = []
#     for i in range(element):
#         list_number = random.sample(range(15), element)
#     return list_number    


def RAN():
    N = int(input('Введите длину списка: '))
    lst = []
    for i in range(N):
        lst.append(random.randint(-N, N))
    return lst

# num = array()
# print(num)
num = RAN()
print(num)
random.shuffle(num)
print(num)
# ist_number = [1, 2, 3, 4, 5, 6]
# random.shuffle(list_number)

# print(list_number)