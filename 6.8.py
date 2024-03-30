import random
numbers = [0]
for i in range(1, 200+1):
    numbers.append(random.randint(1, 200))
    while [i] in numbers:
        numbers.append(random.randint(1, 200))
a = int(input()) - 1
number = numbers[a]
print(number)
