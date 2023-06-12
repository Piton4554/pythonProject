import copy

a = [[1, 2], [1, 4]]
print(id(a[0][1]))
print(id(a[1][1]))
x = [1, 2]
y = [1, 2]
print(id(x[1]))
print(id(y[1]))
y.pop(1)
y.append(10)
print(id(x))
print(id(y))

a = [[1, 2], [10, 23]]
# b = a

# b = []
# b += a

#b = a[::]

b = copy.deepcopy(a)

print(id(a))
print(id(b))
b.pop(1)
print(b)
print(a)