def check():
    output = []
    for i in a:
        output.append(abs(i))
    output.sort()
    b = sorted(a)
    for i in b:
        if i < 0:
            output[output.index(abs(i))] = i
        else:
            break
    print(output)


a = (-20, -5, 10, 15, 9)
check()
