gvozdi = [int(i) for i in input().split()]
# gvozdi = list(map(int, input().split()))
gvozdi.sort()
print(gvozdi)
cm = [100000] + [gvozdi[1] - gvozdi[0]] + [0] * (len(gvozdi) + 1)
for i in range(2, len(gvozdi)):
    cm[i] = min(cm[i - 1], cm[i - 2]) + (gvozdi[i] - gvozdi[i - 1])
print(cm)
