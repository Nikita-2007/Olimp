x = int(input())
for i in range(3):
	if x % 3 == 0:
		print(i + x // 3)
	x -= 5
