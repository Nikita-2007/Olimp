for i in range(int(input())):
	l, r = map(int, input().split())
	print(((r+r%2)**2-(l-l%2)**2)//4)



#for i in range(int(input())):
#	l, r = map(int, input().split())
#	for j in range(l-l%2+1, r+1, 2):
#		s += j
#	print(s)
#	s = 0
