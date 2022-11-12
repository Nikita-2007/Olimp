n, m = map(int, input().split())
arr = []
st = res = 0
for i in range(n):
	arr.append(list(map(int, input().split())))
	r = 1e10
	for j in range(m):
		if r > arr[i][j]:
			r = arr[i][j]
			yt = i
	if st < r:
		st = r
		y = yt

for i in range(m):
	if st == arr[y][i]:
		for j in range(n):
			if st < arr[j][i]:
				break
			if j == n-1:
				res = str(st)+'\n'+str(y)+' '+str(i)
print(res)
