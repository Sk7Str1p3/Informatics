a = int(input())
b = int(input())
c = int(input())
d = int(input())

if d-b >= 0:
    e = c-a
    f = d-b
    print(e,f)
else:
    e = c-a-1
    f = d-b+100
    print(e,f)
