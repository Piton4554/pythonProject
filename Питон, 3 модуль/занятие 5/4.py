def r():
    global a
    global x, y
    x, y = list(map(int, input().split()))
    a = [["0"] * x for _ in range(y)]
    print(a)
    if x == y:
        a[x[0]][y[0]] = "1"
        x = x[1:]
    elif x < y:
        a[x[0]][y[0]] = "2"
        x = x[1:]


print(r())

x, y = list(map(int, input().split()))
a = [["0"] * x for _ in range(y)]
print(a)
# print(i for i in a)

for i in range(x):
    for j in range(y):
        if i == j:
            a[i][j] = "1"
        elif j < i:
            a[i][j] = "2"

for i in a:
    print("".join(i))


