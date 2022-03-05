N = int(input())
arr = list(map(int, input().split()))
q = int(input())
S = 0
for i in range(q):
    line = list(map(int, input().split()))
    if line[0] == 1:
        arr[(line[1]-1 - S) % N] = line[2]
    else:
        S = (S + line[1]) % N
    print(sum(arr))





##temp = [0]*N
##for j in range(N):
##    temp[j] = arr[(j-line[1]) % N]
##arr = temp
