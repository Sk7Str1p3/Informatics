a = list(map(int,input().split()))
s = 0

for i in range(1, len(a)-1):
    if (a[i-1] < a[i] > a[i+1]):
        s += 1

print(s)

