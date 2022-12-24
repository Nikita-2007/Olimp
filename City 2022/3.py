n = int(input())
arr = list(map(int, input().split()))
s = t = 0
for i in range(n):
	s += arr[i] * (i+1)
x = s
for i in range(n):
	for j in range(i, n):
		t = s - (arr[i]*(i+1) + arr[j]*(j+1)) + (arr[i]*(j+1) + arr[j]*(i+1)) 
		x = max(t, x)
print(x)






#n = int(input())
#arr = list(map(int, input().split()))
#s = t = 0
#for i in range(n):
#	s += arr[i] * (i+1)
#for i in range(n):
#	for j in range(n):
#		arr[i], arr[j] = arr[j], arr[i]
#		for k in range(n):
#			t += arr[k] * (k+1)
#		s = max(s, t)
#		t = 0
#		arr[i], arr[j] = arr[j], arr[i]
#print(s)
