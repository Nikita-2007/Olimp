for i in range(int(input())):
	P, arr = input(), list(map(int, input().split()))
	print((max(arr)-min(arr))*2)
