T = int(input())
for i in range(T):
    s = 0
    L, R = map(int, input().split())
    if L % 2 == 1:
        L -= 1
    if R % 2 == 1:
        R += 1
    print(((L + R) // 2) * ((R-L) // 2))
