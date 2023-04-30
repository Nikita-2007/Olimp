def Kirp(brick):
    A1, B1, A2, B2 = brick.split()
    A1, B1, A2, B2 = int(A1), int(B1), int(A2), int(B2)
    
    if A1>B1:
        H1 = A1
    else:
        H1 = B1
    if A2>B2:
        H2 = A2
    else:
        H2 = B2
    return H1+H2

print(Kirp("1 3 2 2")) # 5
input()

#A1, B1, A2, B2 = input().split()
#if A1) < B1):
#    if A2) < B2):
#        H = B1) + B2)
#    else:
#        H = B1) + A2)
#else:
#    if A2) < B2):
#        H = A1) + B2)
#    else:
#        H = A1) + A2)
#print(H)