n = list(map(int,input().split()))
a = []
ms = 0
mn = 0
s = 0

for x in range(n[0]):
    a.append(list(map(int,input().split())))

for i in range(n[0]):
    s = 0
    for j in range(n[1]):
        s += a[i][j]
        if s > ms:
            ms = s
            mn = i

print(ms)
print(mn)