for i in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	arr.sort(reverse=True)
	s = 0
	for j in range(2, n, 3):
		s += arr[j]
	print(s)
