a = list(map(int,input().split()))
b = int(input())

a = a[:b] + a[(b+1):]

print(*a)


