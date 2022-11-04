n = int(input())
arr = list(map(int, input().split()))

temp = 0
for i in range(n):
	arr[i], temp = arr[i] - temp, arr[i]

for i in range(int(input())):
	l, r, v = map(int, input().split())
	arr[l-1] += v
	if r != n:
		arr[r] -= v

temp = 0
for i in range(n):
	arr[i] += temp
	temp = arr[i]
print(*arr)



#n = int(input())
#arr = list(map(int, input().split()))
#for i in range(int(input())):
#	l, r, v = map(int, input().split())
#	for j in range(l-1, r):
#		arr[j] += v
#print(*arr)
