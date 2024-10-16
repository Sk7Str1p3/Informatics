a = list(map(int, input().split()))
pitr = int(input())

c = 1

for i in a:
    if i > pitr or i == pitr:
        c += 1

print (c)
