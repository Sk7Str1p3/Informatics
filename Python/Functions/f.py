def Stage(a,n):
    a = float(a)
    n = int(n)
    out = 1

    if n >= 1:
        for i in range(0,n):
            out *= a
    
    elif n <= -1:
        for i in range(n,0):
            out /= a

    return out

a,n = input().split()

print(Stage(a,n))