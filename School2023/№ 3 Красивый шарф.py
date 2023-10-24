n = int(input())
m = int(input())
k = int(input())
c = int(input())
s = 0
for i in range(n):
	arr = []
	for j in range(m):
		arr.append((i*n+j)%k+1)
	s += arr.count(c)
print(s)
