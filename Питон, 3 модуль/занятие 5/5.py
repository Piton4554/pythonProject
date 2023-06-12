def check():
    global a
    a = "".join(a)
    w_c = ["012", "345", "678", "036", "147", "256", "048", "246"]
    for i in w_c:
        if a[int(i[0])] == a[int(i[1])] == a[int(i[2])]:
            print(a[int(i[0])])
            break
    else:
        print("D")


a = ["x.o", "xx.", "oo."]
check()
