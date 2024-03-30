cell = input("Введите координаты откуда идет конь и куда: ")
start_sq = cell[0:2]
end_sq = cell[3:5]
print(start_sq)
print(end_sq)
dx = abs(ord(start_sq[0]) - ord(end_sq[0]))
dy = abs(int(start_sq[1]) - int(end_sq[1]))
print(dx)
print(dy)

if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print("верно")
else:
    print("ошибка")