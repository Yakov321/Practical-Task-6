import math

r = 6.5
A = float(input("Введите длину ковровой дорожки (м): "))
B = float(input("Введите ширину ковровой дорожки (м): "))

if 2 * math.sqrt((A / 2) ** 2 + (B / 2) ** 2) <= 2 * r:
    print("Ковровая дорожка поместится на цирковой арене.")
else:
    print("Ковровая дорожка не поместится на цирковой арене.")