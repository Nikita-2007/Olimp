n, arr = int(input()), list(map(int, input().split()))
l, r, m = sum(arr), 0, 1e6
for i in arr:
	l, r = l-i, r+i
	m = min(m, abs(l-r))
print(m)
