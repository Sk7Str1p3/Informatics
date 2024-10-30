n, m = map(int, input().split())
a = [[0]*m for i in range(n)]

for k in range(n*m):
	i = k // m
	j = k % m
	a[i][j] = i * j
	print(a[i][j], end=" ")
	if (j == m - 1):
		print()