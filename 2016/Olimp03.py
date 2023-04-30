#Ввод
N = 10 #input("Деапозон - ")
M = 7 #int(input("Количество цифр - "))
arr = "9 3 6 4 3 2 9" #input("Спискa - ")

#Решение
sumN = 0
arr = arr.split()
setArr = set(arr)
for i in setArr:
    x = arr.count(i)
    if x > sumN:
        maxN = i
        sumN = x
    elif x == sumN and maxN > i:
        maxN = i
  
#Вывод
print(maxN, sumN)
input()

#N = input()
#M = input()
#arr = input()
#sumN = 0
#arr = arr.split()
#setArr = set(arr)
#for i in setArr:
#    x = arr.count(i)
#    if x > sumN:
#        maxN = i
#        sumN = x
#    elif x == sumN and maxN > i:
#        maxN = i
#print(maxN, sumN)