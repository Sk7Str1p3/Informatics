k = int(input())
m = int(input())
n = int(input())
 
if k >= n:
    res = 2*m
else:
    res = (2*n//k)*m
    if n%k != 0 and n%k != k//2:
        res += m
print(res)
