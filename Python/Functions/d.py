def Election(x, y, z):
    s = 0

    tc = sum([x is True, y is True, z is True])
    fc = sum([x is False, y is False, z is False])
    
    if tc > fc:
        s = 1
    else:
        s = 0

    return s

x = int(input())
y = int(input())
z = int(input())

print(Election(x,y,z))
