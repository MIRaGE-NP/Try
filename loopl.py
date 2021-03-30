a = int(input())
b = []
for i in range(0, a):
    c = int(input())
    b.append(c)
d = int(input())
e = 0
for i in range(0,a):
    if b[i] == d :
        e = e+1
if e >= 1 :
    print("Yes")
else :
    print("No")
