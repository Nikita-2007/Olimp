row = []
rowe = []
col = []
cole = []
test = 0
for i in range(3):
	row.append(list(map(int, input().split())))
	
n = (sum(row[0])+sum(row[1])+sum(row[2]))//3
col = [[row[0][0], row[1][0], row[2][0]], [row[0][1], row[1][1], row[2][1]], [row[0][2], row[1][2], row[2][2]]]

for i in range(3):
	if sum(row[i]) != n:
		rowe.append(i)
	if sum(col[i]) != n:
		cole.append(i)
if len(rowe) == 0:
	for i in range(3):
		col[cole[0]][i], col[cole[1]][i] = col[cole[1]][i], col[cole[0]][i]
		if sum(col[cole[0]]) == sum(col[cole[1]]) == n:
			break
		col[cole[0]][i], col[cole[1]][i] = col[cole[1]][i], col[cole[0]][i]
	row = [[col[0][0], col[1][0], col[2][0]], [col[0][1], col[1][1], col[2][1]], [col[0][2], col[1][2], col[2][2]]]
elif len(cole) == 0:
	for i in range(3):
		row[rowe[0]][i], row[rowe[1]][i] = row[rowe[1]][i], row[rowe[0]][i]
		if sum(row[rowe[0]]) == sum(row[rowe[1]]) == n:
			break
		row[rowe[0]][i], row[rowe[1]][i] = row[rowe[1]][i], row[rowe[0]][i]
else:
	row[rowe[0]][cole[0]], row[rowe[1]][cole[1]] = row[rowe[1]][cole[1]], row[rowe[0]][cole[0]]
	if sum(row[rowe[0]]) == sum(row[rowe[1]]) == n:
		test = 1
	if test == 0:
		row[rowe[0]][cole[0]], row[rowe[1]][cole[1]] = row[rowe[1]][cole[1]], row[rowe[0]][cole[0]]
		row[rowe[1]][cole[0]], row[rowe[0]][cole[1]] = row[rowe[0]][cole[1]], row[rowe[1]][cole[0]]
for i in range(3):
	print(*row[i])






#arr = []
#for i in range(3):
#    for j in input().split():
#        arr.append(int(j))
#
#for i in range(9):
#    for j in range(i + 1, 9):
#        arr[i], arr[j] = arr[j], arr[i]
#        if  sum(arr[0:3]) == sum(arr[3:6]) == sum(arr[6:9]) == sum(arr[0:7:3]) == sum(arr[1:8:3]) == sum(arr[2:9:3]) :
#            break
#        else:
#            arr[i], arr[j] = arr[j], arr[i]
#
#for i in range(0, 9, 3):
#    print(arr[i], arr[i + 1], arr[i + 2])
    
    
    
    
