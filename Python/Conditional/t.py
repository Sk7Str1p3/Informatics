a=int(input())
b = int(input())
c = int(input())
d = max(a,b,c)

if d<(a+b+c-d):
    print("YES")
else:
    print("NO")
