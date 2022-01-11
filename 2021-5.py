stroka = input()
s = 0
for i in range(len(stroka)):
    for j in range(i, len(stroka)):
        test = stroka[i:j+1]
        if test == test[::-1]:
            if len(test) > s:
                s = len(test)
print(s)
