N, M = map(int, input().split())
sed, x, y, arr, arr2 = 0, 0, 0, list(), list()
for i in range(N):
    temparr = list(map(int, input().split()))
    arr.append(min(temparr))
    arr2.append(temparr)
    sed = max(arr)
    y = arr.index(sed)
    if arr2[i][y] == sed:
        x = i
print(sed)
print(x, y)
