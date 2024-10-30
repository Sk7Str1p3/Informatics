n, m = map(int, input().split())
A = []

for i in range(n):
    b = list(map(int, input().split()))
    A.append(b)

maxn = 0
maxi = 0
maxj = 0

for i in range(n):
    if max(A[i]) > maxn:
        maxn = max(A[i])
        maxi = i
        maxj =A[i].index(max(A[i]))
print(maxn)
print(maxi, maxj)