A = int(input())
B = int(input())
C = int(input())

if (A % 2 == 1 and B % 2 == 0) or (A % 2 == 0 and B % 2 == 1) or (A % 2 == 1 and C % 2 == 0) or (A % 2 == 0 and C % 2 == 1) or (B % 2 == 1 and C % 2 == 0) or (B % 2 == 0 and C % 2 == 1):
    print("YES")
else:
    print("NO")
