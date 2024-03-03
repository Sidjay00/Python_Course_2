# import random

# def change_elements(numbers, index):
#     return numbers[:index] + (random.randint(1, 10), ) + numbers[index+1:]

# numbers = tuple(random.randint(1,10) for _ in range(10))

# index = 4
# numbers = change_elements(numbers, index)
# print(numbers)

# Задание 2. На ввод подаются 2 числа, нужно сделать метод, который вернёт произведение, сумму, разность и отношение этих двух чисел


def method(a,b):
    return a*b, a+b, a-b, a/b

a, b = 10, 2
numbers = method(a, b)
summ, diff, multiplication, div = method(a, b)
print(numbers)
print(type(numbers))
print(summ, diff, multiplication, div)