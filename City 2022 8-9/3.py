n = int(input())
arr = []
d = 100
s = 0
temp = False
for i in range(n):
	arr.append(input())
	d = min(d, len(arr[i]))
for i in range(d):
	c = arr[0][i]
	s += 1
	for j in range(1, n):
		if c != arr[j][i]:
			s -= 1
			temp = True
			break
	if temp:
		break
print(s)
