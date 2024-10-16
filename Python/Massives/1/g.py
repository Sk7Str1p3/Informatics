a = list(map(int,input().split()))
im = 0

for i in range(1, len(a)):
    if a[i] > a[im]:
        im = i
print(a[im], im)

