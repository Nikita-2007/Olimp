n = input()
r1 = r2 = l1 = l2 = 0
for i in range(3):
	if n[i] != '*':
		r1 += int(n[i])
		l1 += int(n[i])
	else:
		r1 += 9
for i in range(3, 6):
	if n[i] != '*':
		r2 += int(n[i])
		l2 += int(n[i])
	else:
		r2 += 9
if r1 < l2 or r2 < l1:
	print('No')
else:
	print('Yes')
