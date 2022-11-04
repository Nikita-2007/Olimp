r, l = map(int, input().split())
temp = 0

for i in range(r, l):
	s = str(i*i)
	if i == int(s[len(s) - len(str(i)):]):
	  print(i)
	  temp = ''
print(temp)
