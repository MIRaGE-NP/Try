a = []
i = 0
while i > -1 :
    w = int(input())
    a.append(w)
    if w == 0 :
        break
a.remove(0)
b = str(input())
if b == 'MaX':
    a.sort(reverse=True)
    print(*a, sep=", ")
elif b == 'Min' or b == 'min':
    a.sort()
    print(*a, sep=" ")
