N, M = map(int, input().split())
arr = []
sed = 0
arrMin = []

for y in range(N):
    line = list(map(int, input().split()))
    arr.append(line)
    arrMin.append(min(arr[y]))

sed = max(arrMin)
sedY = arrMin.index(sed)
for i in range(N):
    if arr[sedY][i] == sed:
        sedX = i
        break

if sed != 0:
    print(sed)
    print(sedY, sedX)
else:
    print(0)


#5 6
#2 3 2 3 2 5
#1 2 1 2 1 3
#9 8 9 8 5 6
#3 4 3 4 3 4
#2 1 2 1 2 3
