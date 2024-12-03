def phi(n):
    f1 = f2 = 1

    for i in range(n-1):
        f1, f2 = f2, f1 + f2

    return f2

n = int(input())

print(phi(n))