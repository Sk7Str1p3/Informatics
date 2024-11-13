def xor(x,y):
    if x != y:
        out = 1
    else:
        out = 0
    return out

x,y = list(map(int,input().split()))
print(xor(x,y))