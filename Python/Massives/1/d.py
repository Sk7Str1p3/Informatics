a = list(map(int,input().split()))
n = 0

for i in range(1, len(a)):
    if a[i] > a[i-1]:
        n = a[i]
        print(n)
