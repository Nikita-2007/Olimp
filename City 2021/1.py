arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
d1 = d2 = 0
for i in range(3):
	if arr1[i]>arr2[i]:
		d1 += 1
	elif arr1[i]<arr2[i]:
		d2 += 1
if d1>d2 and d1 >=2:
	print(1)
elif d2>d1 and d2 >= 2:
	print(2)
else:
	print(0)
