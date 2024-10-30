n, m = map(int, input().split())
A = []
C = []

for i in range(n): # формирование матрицы A
	b = list(map(int, input().split())) # считывается по-строчно с формированием списка
	A.append(b)

max_zn = 0
max_sum = 0
max_i = 0
max_j = 0

for i in range(n):
	if (max(A[i]) > max_zn):
		max_zn = max(A[i])

for i in range(n):
	if (max_zn in A[i]):
		C.append(i)	# массив строк, где есть максимальное значение

print(len(C))
print(*C)