cell = input("Введите координаты клетки: ")
column = ord(cell[0]) - ord('b')
row = int(cell[1])
print(ord(cell[0]))
if (column + row) % 2 == 0:
    print("Черный")
else:
    print("Белый")
