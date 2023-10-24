n = int(input())
arr = []
s = 0
while s < n:
    m = min(n - s, s + 1)
    arr.append(m)
    s += m
print(*arr)
