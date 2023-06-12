def cheat(n: int, s, f):
    global x
    x += 1

    # n = str(n)
    try:
        if not str(n).isdigit():
            raise ImportError
        if n < 0:
            raise ZeroDivisionError
        if n > 0:
            stolb = 6 - s - f
            cheat(n - 1, s, stolb)
            x += 1
            print(f"Перенести диск{n} cо стержня {s} на стержень {f}")
            cheat(n - 1, stolb, f)


    except ImportError:
        print("Нельзя буквы")
    except ZeroDivisionError:
        print("Нельзя 0")
    except:
        print("боль")


x = 0
cheat(3, 1, 3)
print(x)
