x, N, A = 0, int(input()), list(map(int, input().split()))
for i in range(N):
    if A[i] < 0:
        x += 1
print(x)
if x > int(input()):
    print(abs(min(A)))
