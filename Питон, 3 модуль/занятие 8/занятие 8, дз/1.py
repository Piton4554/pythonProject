def capibara(horo):
    x = [0] * (horo + 1)
    x[0] = 1
    x[1] = 1
    x[2] = 2

    for i in range(3, horo + 1):
        x[i] = ((x[i - 1] + x[i - 2]) + 1)
    print(x)
    return x[horo]


print(capibara(4))
