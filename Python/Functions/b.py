def stage( a, n ):
    out = 1
    for i in range(n):
        out *= a
    return out

a,n = input().split()
if '.' in a:
    a = float(a)
else:
    a = int(a)
n = int(n)

print(stage(a,n))