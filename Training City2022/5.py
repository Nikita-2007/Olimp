s = '-'+'-'.join(input())+'-'
maxi = 0
d = len(s)
for i in range(d):
	n = -1
	for j in range(min(i, d-i-1)+1):
		if s[i-j] == s[i+j]:
			n += 1
		else:
			break
	maxi = max(maxi, n)
print(maxi)







#s = input()
#maxi = 0
#for i in range(len(s)):
#	for j in range(i, len(s)):
#		test = s[i:j+1]
#		if test == test[::-1]:
#			maxi = max(maxi, (len(test)))
#print(maxi)
