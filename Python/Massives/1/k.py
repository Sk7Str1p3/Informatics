a = list(map(int,input().split()))
n = 1

for i in range(1, len(a)):
    if a[i] != a[i-1]:
        n += 1

print(n)
