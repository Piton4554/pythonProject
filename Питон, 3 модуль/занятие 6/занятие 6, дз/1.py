import time

a = [34, 56, 78, 9, 0, 4, -6, -78, 90]
a.sort()
b = sorted(a)

start1 = time.perf_counter()
print(a)
finish1 = time.perf_counter()
# 2.519999907235615e-05

start2 = time.perf_counter()
print(b)
finish2 = time.perf_counter()
# 1.1000000085914508e-05

print(finish1 - start1)
print(finish2 - start2)



