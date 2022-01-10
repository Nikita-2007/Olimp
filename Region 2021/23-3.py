N, arrb, arrm = int(input()), list(), list()
for i in range(N):
    x, z = map(str, input().split())
    x = int(x)
    if z == '>':
        arrb.append(x)
    else:
        arrm.append(x)
print(min(arrb)-max(arrm))
