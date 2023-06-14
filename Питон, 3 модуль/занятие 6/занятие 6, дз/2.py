def checkio(values):
    return sorted(values, key=abs)


print(checkio([-20, -5, 10, 15]))
print(checkio([1, 2, 3, 0]))
print(checkio([-1, -2, -3, 0]))
