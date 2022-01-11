s = input()
s2 = input()
l = 0
str1 = 'qwertyuiopasdfghjklzxcvbnm'
for i in str1:
    if i in s and i in s2:
        l = l+1
print(l)