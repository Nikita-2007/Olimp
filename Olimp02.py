def Thar(x):
    x = list(str(x))
    x.sort(reverse=True)
    return "".join(x)

print(Thar(56701)) # 76510
input()

#x = input()
#x = list(str(x))
#x.sort(reverse=True)
#print("".join(x))