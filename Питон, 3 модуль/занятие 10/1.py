import random

x, y = list(map(int, input().split()))
kletka = [[1] * y for _ in range(x)]
print(kletka)
for i in range(1, x):
    for j in range(1, y):
        kletka[i][j] = kletka[i - 1][j] + kletka[i][j - 1]
print(kletka)

map_bomb = [[1] * y for _ in range(x)]
map_bomb[1][4] = 0
map_bomb[2][1] = 0
map_bomb[2][3] = 0

map_money = [[random.randint(-10, 100) for _ in range(y)] for _ in range(x)]
potratil = [map_money[0][0] * y for _ in range(x)]

kletka2 = [1] * y
print(kletka2)
for j in range(1, x):
    for i in range(1, y):
        kletka2[i] = (kletka2[i] + kletka2[i - 1]) * map_bomb[j][i]
    #print(kletka2)
