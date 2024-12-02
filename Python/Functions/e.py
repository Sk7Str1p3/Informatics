def Prime(n):
    if n <= 1:
        return "composite"  # Числа <= 1 не являются простыми
    if n <= 3:
        return "prime"  # 2 и 3 - простые числа
    if n % 2 == 0 or n % 3 == 0:
        return "composite"  # Исключаем четные числа и кратные 3

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return "composite"
        i += 6

    return "prime"

n = int(input())

print(Prime(n))
