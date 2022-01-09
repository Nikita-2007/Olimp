arr = list(map(str, input().split()))
arr.sort()
for i in range(317, 1000):
    arrtemp = list(str(i*i))
    arrtemp.sort()
    if arr == arrtemp:
        print(i*i)
        break
