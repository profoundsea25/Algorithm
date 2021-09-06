from itertools import combinations
#n=5; data = [[X,S,X,X,T],[T,X,S,X,X],[X,X,X,X,X],[X,T,X,X,X],[X,X,T,X,X]]
#n=4; data = [[S,S,S,T],[X,X,X,X],[X,X,X,X],[T,T,T,X]]
n = int(input())
data = []
nothing = []
teacher = []
for i in range(n):
    data.append(list(map(str, input().split())))
    for j in range(n):
        if data[i][j] == "T":
            teacher.append((i,j))
        elif data[i][j] == "X":
            nothing.append((i,j))

wall = list(combinations(nothing, 3))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def dfs(x,y,test):
    for i in range(4):
        nx = x
        ny = y
        while(nx >= 0 and nx < n and ny >= 0 and ny < n):
            if test[nx][ny] == "S":
                return False
            if test[nx][ny] == "O":
                break
            nx += dx[i]
            ny += dy[i]
    return True

i = 0
test = [[0]*n for _ in range(n)]
while(i < len(wall)):
    for l in range(n):
        for k in range(n):
            test[l][k] = data[l][k]
    test[wall[i][0][0]][wall[i][0][1]] = "O"
    test[wall[i][1][0]][wall[i][1][1]] = "O"
    test[wall[i][2][0]][wall[i][2][1]] = "O"
    check = 0
    for m in range(len(teacher)):
        if dfs(teacher[m][0],teacher[m][1], test) == True :
            check += 1
        else :
            break
    if check == len(teacher):
        break
    i += 1

if check == len(teacher):
    print("YES")
else :
    print("NO")