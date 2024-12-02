def Election(x, y, z):
    x = int(x)
    y = int(y)
    z = int(z)
    s = x + y + z

    if s >= 2:
        return 1
    else:
        return 0

x, y, z = input().split()

print(Election(x, y, z))
