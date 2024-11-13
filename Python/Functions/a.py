def min(a1, b1):
    c = a1
    if b1 < c: c = b1
    return c

a,b,c,d = list(map(int,input().split()))

print(min(min(a,b), min(c,d)))

