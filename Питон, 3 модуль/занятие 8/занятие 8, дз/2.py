somnitelno = int(input())
lst = [0] * (somnitelno + 1)
lst[0] = 1
lst[1] = 2
lst[2] = 4
if somnitelno == 1 or somnitelno == 2:
    print(somnitelno)
elif somnitelno == 3:
    print(4)
else:
    lst[0] = 1
    lst[1] = 2
    lst[2] = 4
    for i in range(3, somnitelno + 1):
        lst[i] = (lst[i - 1] + lst[i - 2] + lst[i - 3])

print(lst[somnitelno - 1])