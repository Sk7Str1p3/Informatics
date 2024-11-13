a = int(input())
b = int(input())
c = int(input())
d= int(input())

def min(a, b, c, d):
    out = [a,b,c,d]
    out.sort()
    return out[0]

print(min(a,b,c,d))
