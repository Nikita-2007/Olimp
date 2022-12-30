n = int(input())
arr = list(map(int, input().split()))
for i in range(n-1):
	if i & 1:
		if arr[i] > arr[i+1]:
			arr[i], arr[i+1] = arr[i+1], arr[i]
	else:
		if arr[i] < arr[i+1]:
			arr[i], arr[i+1] = arr[i+1], arr[i]
print(*arr)
