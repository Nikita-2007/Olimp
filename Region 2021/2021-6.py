x = input()
k = int(input())
if k == 0:
    n = x[0]
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
    pass

