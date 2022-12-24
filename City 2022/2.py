a = list(set(input()))
a.sort()
b = list(set(input()))
c = ''
for i in a:
	if i in b:
		c += i
if c == '':
	c = 'epidemic'
print(c)
