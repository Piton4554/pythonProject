import random

n = int(input())
buy = [0] * 3 + [random.randint(-100, 100) for _ in range(n + 1)]
print(buy)
for i in range(2, n + 3):
    buy[i] += min(buy[i - 3], buy[i - 2], buy[i - 1])
print(buy[-2])
print(buy)