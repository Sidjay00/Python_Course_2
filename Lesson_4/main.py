import random

def change_elements(numbers, index):
    return numbers[:index] + (random.randint(1, 10), ) + numbers[index+1:]

numbers = tuple(random.randint(1,10) for _ in range(10))

index = 4

print(numbers)
numbers = change_elements(numbers, index)
print(numbers)
print(type(numbers))