import random

n = int(input())
buy = [0] + [random.randint(-11, 10) for i in range(n + 1)]
print(buy)
seil = [0] * (n + 1)
seil[1] = buy[1]
for i in range(2, n + 1):
    seil[i] = buy[i] + min(buy[i - 1], buy[i - 2])

print(seil)
m = 0
# for i in range(len(seil)):
while n > 0:
    if seil[n - 1] > seil[n - 2]:
        n -= 2
        print("-2")

    if seil[n - 1] < seil[n - 2]:
        # m += seil[n - 1]
        n -= 1
        print("-1")

print(seil[n])