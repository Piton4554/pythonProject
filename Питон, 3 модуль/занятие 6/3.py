def anagram(t1, t2):
    return sorted(str(t1.replace("", "").lower())) == sorted(str((t2.replace("", "").lower())))


x, y = input().split(",")

print(x)
print(y)
print(anagram(x, y))