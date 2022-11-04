x1, y1, x2, y2 = map(int, input().split())
a = (y1 - y2)//(x1 - x2)
b = y2-x2*a;
if b >= 0:
	z = '+'
else:
	z = '-'
b = abs(b)

print('y='+str(a)+'x'+str(z)+str(b));
