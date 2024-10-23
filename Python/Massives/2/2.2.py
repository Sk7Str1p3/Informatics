n = int(input())
A = []

for i in range(n):
    m = list(map(int,input().split()))
    A.append(m)

for x in range(n):
    for y in range(n):
        if A[x][y] != A[y][x]:
            print("no")
            exit()

print("yes")
        