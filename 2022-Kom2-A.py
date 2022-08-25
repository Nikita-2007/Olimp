a, b = map(int, input().split())
s = min(a%b, b-a%b)
for i in range(s):
	Bp = (b+i)
	Bm = (b-i)
	s = min(s, a%Bp+i, a%Bm+i, Bp-a%Bp+i, Bm-a%Bm+i)
print(s)
