# Q 11 뱀, p.327 / 521

n = int(input())
k = int(input())
klist = []
for _ in range(k):
    klist.append(list(map(int, input().split())))
l = int(input())
llist = []
for _ in range(l) :
    llist.append(list(map(str, input().split())))

board = [[0] * n for _ in range(n)]

for x in klist:
    board[x[0]-1][x[1]-1] = 2
board[0][0] = 1

count = 0
length = []
x = 0
y = 0
i = 0
j = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
length.append([0,0])

while True :
    count += 1
    x += dx[i]
    y += dy[i]
    length.append([x, y])
    if x < 0 or x >= n or y < 0 or y >= n :
        break
    elif board[x][y] == 1 :
        break
    elif board[x][y] == 2 :
        board[x][y] = 1
    elif board[x][y] == 0 :
        board[x][y] = 1
        temp = length.pop(0)
        board[temp[0]][temp[1]] = 0
    
    if count == int(llist[j][0]):
        if llist[j][1] == 'D':
            i += 1
        else :
            i -= 1
        
        if i == -1:
            i = 3
        elif i == 4:
            i = 0
        if j < len(llist)-1:
            j += 1

print(count)