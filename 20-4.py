N = int(input())
T = int(input())
maxi = start = 0

for i in range(T):
    K, S = map(int, input().split())
    maxi = (N-(K*2-1))*4
    start = (maxi - S+1) % maxi
    print(start, maxi)
