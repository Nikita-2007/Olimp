x = input()
k = int(input())
n = x[0]
if k == 0:
    for i in x:
        if i == n:
            continue
        elif i < n:
            break
        else:
            n = str(int(n)+1)
            break
    print(n*len(x))
else:
    while True:
        if max(x.count(x[0]), x.count(x[-1])) >= len(x) - 1:
            print(x)
            break
        else:
            x = str(int(x) +1)
