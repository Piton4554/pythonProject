import time


def sortt():
    for i in range(1, len(a)):
        e = a[i]
        j = i - 1

        while j >= 0 and e < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = e
    global start1, finish1
    start1 = time.perf_counter()
    print(a)
    finish1 = time.perf_counter()
    print(finish1 - start1)
    # 2.4900000425986946e-05


a = [5, 3, 0, 0, 4, 1, 4, 0, 7]
sortt()
