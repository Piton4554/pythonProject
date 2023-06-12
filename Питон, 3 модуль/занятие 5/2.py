# print([["a"]] * 10)

a = [[0] * 3] * 3
print(a)
a[0].pop(0)
a[0].append(10)
print(a)

b = [0] * 3
for i in range(3):
    b[i] = [0] * 3

b[0].pop(0)
print(b)

c = [0] * 3
c = [[0] * 4 for i in range(len(c))]
