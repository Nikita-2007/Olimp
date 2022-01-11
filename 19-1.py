x = int(input())
if x % 4 == 0:
    print(-x)
elif (x + 1) % 4 == 0:
    print(0)
elif (x + 2) % 4 == 0:
  print(x+1)
else:
    print(1)