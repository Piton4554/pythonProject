a = [[1, 2], [3, 4]]
for i in range(len(a)):
    a[i] = a[i][::-1]

print(a[::-1])