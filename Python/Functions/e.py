def Prime(n):
    l = 0
    o = "foo"

    if n == 1 or n == 0:
        o = "Prime"
    else:
        for i in range(1,n):
            if n % i == 0:
                l += 1
        if l == 1:
            o = "Prime"
        else:
            o = "Composite"

    return o

n = int(input())

print(Prime(n))
