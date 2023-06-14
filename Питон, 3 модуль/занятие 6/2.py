import random


def bubble_sort(lst):
    for j in range(len(lst)):
        f = True
        for i in range(len(lst)-1-j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                f = False
        if f:
            break
    print(lst)


lst = [random.randint(-100, 100) for _ in range(10000)]
bubble_sort(lst)