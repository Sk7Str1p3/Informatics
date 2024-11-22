N = int(input())

if N % 10 == 1 and N % 100 != 11:
    print(N, "bochka")

elif N % 10 == 0 or 5 <= N % 10 <= 9 or (11 <= N % 100 <= 19):
    print(N, "bochek")

#if 2 <= N % 10 <= 4 and (12 <= N % 100 <= 19):
else:
    print(N, "bochki")
