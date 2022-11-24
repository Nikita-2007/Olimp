arr = []
n = int(input())
arrN = list(map(int, input().split()))
m = int(input())
arrM = list(map(int, input().split()))
arrN.sort()
arrM.sort()
k = int(input())
while len(arr) < k:
	for j in range(m):
		if arrN[i] < arrM[j]:
			break
		arrN[i]



#arr = []
#n = int(input())
#arrN = list(map(int, input().split()))
#m = int(input())
#arrM = list(map(int, input().split()))
#k = int(input())-1
#for i in range(n):
#	for j in range(m):
#		arr.append(arrN[i]+arrM[j])
#arr.sort()
#print(arr[k])
