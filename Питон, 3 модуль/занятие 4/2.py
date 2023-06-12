import math


def nod(x, y):
    if y == 0:
        return x
    else:
        return nod(y, x % y)


print(math.gcd(7, 14))
print(nod(7, 14))
print(7 % 14)
