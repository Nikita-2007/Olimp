n, maxi, s, arr = input(), 1, 1, list(map(int, input().split()))
for i in range(len(arr)-1):
	s += 1 if arr[i] >= arr[i+1] else 1
	maxi = max(maxi, s)
print(maxi)
