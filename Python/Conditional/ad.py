X = int(input())

x1 = X // 10
x2 = X % 10

if 0 <= x2 <= 3:
    x2 *= "I"
elif x2 == 4:
    x2 = "IV"
elif 5 <= x2 <= 8:
    x2 = "V" + (x2-5) * "I"
elif x2 == 9:
    x2 = "IX"

if 0 <= x1 <= 3:
    x1 *= "X"
elif x1 == 4:
    x1 = "XL"
elif 5 <= x1 <= 8:
    x1 = "L" + (x1-5) * "X"
elif x1 == 9:
    x1 = "XC"
elif 10 <= x1 <= 13:
    x1 = "C" + (x1-10) * "X"
elif x1 == 14:
    x1 = "CXL"
elif 15 <= x1 <= 18:
    x1 = "CL" + (x1-15) * "X"
elif x1 == 19:
    x1 = "CXC"


print(x1,x2, sep = '')
