M,N = input().split()
x,y = input().split()

M = int(M)
N = int(N)
x = int(x)
y = int(y)

# y(N)
# ^ * 1 *
# | 2 0 4
# | * 3 *
#    ==> x(M)
x1 = x 
y1 = (y + 1)
x2 = (x - 1)
y2 = y
x3 = x
y3 = (y - 1)
x4 = (x + 1)
y4 = y

if x1 > 0 and x1 <= M and y1 > 0 and y1 <= N:
    print(x1,y1)
if x2 > 0 and x2 <= M and y2 > 0 and y2 <= N:
    print(x2,y2)
if x3 > 0 and x3 <= M and y3 > 0 and y3 <= N:
    print(x3,y3)
if x4 > 0 and x4 <= M and y4 > 0 and y4 <= N:
    print(x4,y4)
