arr = [0] * 9
n = int(input())
for i in range(n):
    s = int(input())
    if s == 0:
        arr[0] = arr[1] = arr[3] = arr[5] = arr[7] = arr[8] = 1
    elif s == 1:
        arr[2] = arr[3] = arr[7] = 1
    elif s == 2:
        arr[0] = arr[3] = arr[6] = arr[8] = 1
    elif s == 3:
        arr[0] = arr[2] = arr[4] = arr[6] = 1
    elif s == 4:
        arr[1] = arr[3] = arr[4] = arr[7] = 1
    elif s == 5:
        arr[0] = arr[1] = arr[4] = arr[7] = arr[8] = 1
    elif s == 6:
        arr[2] = arr[4] = arr[5] = arr[7] = arr[8] = 1
    elif s == 7:
        arr[0] = arr[2] = arr[5] = 1
    elif s == 8:
        arr[0] = arr[1] = arr[3] = arr[4] = arr[5] = arr[7] = arr[8] = 1
    elif s == 9:
        arr[0] = arr[1] = arr[3] = arr[4] = arr[6] = 1
if arr[0] == 1 and arr[1] == 1 and arr[3] == 1 and arr[5] == 1 and arr[7] == 1 and arr[8] == 1:
    print(0)
if arr[2] == 1 and arr[3] == 1 and arr[7] == 1:
    print(1)
if arr[0] == 1 and arr[3] == 1 and arr[6] == 1 and arr[8] == 1:
    print(2)
if arr[0] == 1 and arr[2] == 1 and arr[4] == 1 and arr[6] == 1:
    print(3)
if arr[1] == 1 and arr[3] == 1 and arr[4] == 1 and arr[7] == 1:
    print(4)
if arr[0] == 1 and arr[1] == 1 and arr[4] == 1 and arr[7] == 1 and arr[8] == 1:
    print(5)
if arr[2] == 1 and arr[4] == 1 and arr[5] == 1 and arr[7] == 1 and arr[8] == 1:
    print(6)
if arr[0] == 1 and arr[2] == 1 and arr[5] == 1:
    print(7)
if arr[0] == 1 and arr[1] == 1 and arr[3] == 1 and arr[4] == 1 and arr[5] == 1 and arr[7] == 1 and arr[8] == 1: 
    print(8)
if arr[0] == 1 and arr[1] == 1 and arr[3] == 1 and arr[4] == 1 and arr[6] == 1:
    print(9)
