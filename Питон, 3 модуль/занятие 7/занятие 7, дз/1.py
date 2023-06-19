x = [int(x) for x in input().split()]
lst = []
while True:
    try:
        lst.append(x.index(0) + len(lst))
        x.pop(x.index(0))
    except:
        break

x.sort()
for i in lst:
    x.insert(i, 0)

print(x)
print(lst)
