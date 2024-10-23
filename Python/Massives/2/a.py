n = int(input())
a = [[0] * n for _ in range(n)]

for i in range(0, n):
    for j in range(0,n):
        if j + i == n -1:
            a[i][j] = 1
        if j + i < n - 1:
            a[i][j] = 0
        if j + i > n -1:
            a[i][j] = 2

for r in a:
    print(*r)
