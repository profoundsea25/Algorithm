m, n = map(int, input().split())

data = []
for i in range(n) :
    data.append(list(map(int,input().split())))

one = []
day = 0

for i in range(n):
    for j in range(m):
        if data[i][j] == 1 :
            one.append((i,j))

def tomato(i, j):
    global data
    new_one = []
    data[i][j] = 2
    if i+1 < n and data[i+1][j] == 0 :
        data[i+1][j] = 1
        new_one.append((i+1, j))
    if i > 0  and data[i-1][j] == 0 :
        data[i-1][j] = 1
        new_one.append((i-1, j))
    if j+1 < m and data[i][j+1] == 0 :
        data[i][j+1] = 1
        new_one.append((i, j+1))
    if j > 0 and data[i][j-1] == 0 :
        data[i][j-1] = 1
        new_one.append((i, j-1))
    return new_one

while True :
    new_one = []
    for i in range(len(one)):
        x, y = one.pop()
        new_one += tomato(x, y)
    one = new_one[:]
    
    if not one :
        break
    day += 1

check_zero = True
for i in range(n):
    for j in range(m):
        if data[i][j] == 0 :
            check_zero = False
            break
    if not check_zero :
        break
if check_zero : 
    print(day)
else :
    print(-1)