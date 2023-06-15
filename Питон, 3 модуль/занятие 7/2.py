import time


def droblen(lst):
    while len(lst) != 1:
        return lst[:len(lst) // 2], lst[len(lst) // 2:]


def sorttt(a):
    if len(a) <= 1:
        return a
    return ob(droblen(a)[0], droblen(a)[1])


def ob(x: list, y: list):
    print(x)
    print(y)
    # if x:
    # return sorttt(x)
    # print(y)
    # if y:
    # return sorttt(y)
    if len(x) == 0:
        return y
    if len(y) == 0:
        return x
    b = []
    i_x = i_y = 0
    while len(b) < len(x) + len(y):
        if x[i_x] <= y[i_y]:
            b.append(x[i_x])
            i_x += 1
        else:
            b.append(y[i_y])
            i_y += 1
        if len(x) == i_x:
            b += y[i_y:]
            break
        if len(y) == i_y:
            b += x[i_x:]
            break
    return b


a = [67, 82, 32]
start1 = time.perf_counter()
print(sorttt((a)))
finish1 = time.perf_counter()
print(finish1 - start1)
# 5.690000034519471e-05
