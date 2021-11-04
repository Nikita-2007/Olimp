N = int(input())

arrtoo = []
arrone = []
max_count_1 = 0
max_count_2 = 0

for i in range(N):
    temp = input()
    count = i % 2
    for j in temp:
        count += 1
        if count % 2 == 1:
            arrone.append(j)
        else:
            arrtoo.append(j)

for i in arrone:
    if max_count_1 < arrone.count(i):
        max_count_1 = arrone.count(i)
for i in arrtoo:
    if max_count_2 < arrtoo.count(i):
        max_count_2 = arrtoo.count(i)

print((len(arrone) - max_count_1) + (len(arrtoo) - max_count_2))