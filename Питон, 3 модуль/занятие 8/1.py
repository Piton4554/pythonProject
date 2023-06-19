import time


def f(color_bum):
    print(color_bum, end=" | ")
    if color_bum == 0 or color_bum == 1:
        return color_bum
    else:
        return f(color_bum - 1) + f(color_bum - 2)


def capibara(horo):
    x = [0] * (horo + 1)
    x[1] = 1
    karta_kaktusov = [1] * (horo + 1)
    karta_kaktusov[int(input("где кактусы?"))] = 0
    karta_kaktusov[int(input("где кактусы?"))] = 0
    for i in range(2, horo + 1):
        x[i] = (x[i - 1] + x[i - 2]) * karta_kaktusov[i]
    print(x)
    return x[horo]


# start_r = time.time()

#print(f(6))
print(capibara(8))