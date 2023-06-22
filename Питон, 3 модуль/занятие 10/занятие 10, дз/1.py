def fs(a):
    for i in a:
        if i % 3 == 0:
            return a.sort()
        if i % 3 != 0:
            b.append(i)
            del a[i]
            b.sort()
            a.append(i)
            return a




a = [-10, 0, 7, -2, 3, 6, -8]
b = []

print(fs(a))
print(fs(b))
