n = int(input())
k = int(input())
s = n//k
if n%k == 0:
	s += k-1
else:
	s += k
print(s)
