for i in range(int(input())):
	n, a = map(int, input().split())
	x = ''
	for j in range(n):
		x = x+'1'
	y = int(x)*a
	z = 0
	for j in str(y):
		z += int(j)
	print(z)
