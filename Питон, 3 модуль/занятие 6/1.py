def fs(x):
    return x % 2 == 0


a = [1, 2, 3, 4, -5, 78, 7335, 6, 644]
b = [[1, 2], [4, 3, 2, 1], [2]]

a.sort(key=fs)
print(a)


def fs2(x):
    x = fs3(x)
    return len(x)


def fs3(x):
    x.sort()
    return x


b.sort(key=fs2, reverse=True)
print(b)

c = ["asdsdfghgfds", "asdfgh"]
c.sort(key=lambda fs4: [])
print(c)

d = ("ldfghgds", "adfghjkmnbvds")
h = sorted(d, key=lambda fs4: (len(fs4[0])))
print(h)