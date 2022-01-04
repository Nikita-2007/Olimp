t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    k = n*m
    S = int((1 + k)*k/2)
    pS = S / 2
    V = m // 2
    col1 = int((1 + (n - 1) * m + 1) * n / 2)
    colV = int((V + (n - 1) * m + V) * n / 2)
    colV2 = int(((V+1) + (n - 1) * m + (V+1)) * n / 2)
    vS = int((col1 + colV) * V / 2)
    vS2 = int((col1 + colV2) * (V+1) / 2)
    vR = abs(pS - vS)
    vR2 = abs(pS - vS2)
    if vR <= vR2:
        minV = vR
        col = V+1
    else:
        minV = vR2
        col = V+2

    H = round(n * 0.7066667) #ДОДЕЛАТЬ
    hS = int((H * m / 2) * (H*m+1))
    hS2 = int(((H+1) * m / 2) * ((H+1)*m+1))
    hR = abs(pS - hS)
    hR2 = abs(pS - hS2)
    if hR <= hR2:
        minH = hR
        row = H+1
    else:
        minH = hR2
        row = H+2

    if minH <= minV:
        print('H', row)
    else:
        print('V', col)
