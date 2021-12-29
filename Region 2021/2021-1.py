k = int(input())
a, x = map(int, input().split())
b, y = map(int, input().split())
print(max(max(0, k-b)*y+max(0, k-b-a)*x, max(0, k-a)*x+max(0, k-b-a)*y))
