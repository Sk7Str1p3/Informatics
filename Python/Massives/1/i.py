a = list(map(int,input().split()))
min = float('inf')

for i in a:
    if i < min and i % 2 != 0:
        min = i

if min == float('inf'):
    min = 0

print(min)
