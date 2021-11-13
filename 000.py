N = int(input())
arr = list(map(int, input().split()))
T = int(input())
for i in range(T):
    L, R, V = map(int, input().split())
    for j in range(L-1, R):
        arr[j] += V
print(*arr)
