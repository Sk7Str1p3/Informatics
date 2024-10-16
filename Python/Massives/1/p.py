a = list(map(int,input().split()))
i_min = 0
i_max = 0

for i in range (1, len(a)):
    if a[i] > a[i_max]:
        i_max = i
    if a[i] < a[i_min]:
        i_min = i

a[i_min], a[i_max] = a[i_max], a[i_min]

print(*a)
