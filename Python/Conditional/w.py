a = int(input())
b = int(input())
c = int(input())

sides = sorted([a, b, c])

if sides[0] <= 0:
    print("impossible")

if sides[0] + sides[1] <= sides[2]:
    print("impossible")

if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("right")
elif sides[0]**2 + sides[1]**2 > sides[2]**2:
    print("acute")
else:
    print("obtuse")


