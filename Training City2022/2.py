for i in range(int(input())):
	n = int(input())
	if round(n ** (1.0/3.0)) ** 3 == n:
		print('YES')
	else:
		print('NO')
