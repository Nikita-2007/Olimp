t = int(input())
r = 0
arr = list(map(int, input().split()))
for i in range(t):
    if arr[i] > i+1:
		r += arr[i]
print(r)
