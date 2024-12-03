def fastStage(a,n):
    a = float(a)
    n = int(n)
    out = 1

    if n == 0:
        return 1
    if n == -1:
        return 1. / a
    out = fastStage(a, n // 2)
    out *= out
    if n % 2:
        out *= a

    return out

a,n = input().split()

print(fastStage(a,n))
