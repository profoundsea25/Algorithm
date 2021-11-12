import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(list(input()))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

check = "No"
k = 1

def first(x,y,check_list):
    global k
    global check
    if check == "Yes" :
        return
    if check_list[x][y] != 0:
        return
    check_list[x][y] = k
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and ny >= 0 and nx < n and ny < m and check_list[nx][ny] == 0 :
            if data[x][y] == data[nx][ny] :
                dfs(x,y,nx,ny,check_list)

def dfs(x,y,nx,ny,check_list):
    global k
    global check
    if check == "Yes" :
        return
    check_list[nx][ny] = k

    for i in range(4):
        nnx = nx + dx[i]
        nny = ny + dy[i]
        if nnx >= 0 and nny >= 0 and nnx < n and nny < m :
            if not(nnx == x and nny == y) :
                if check_list[nnx][nny] == k :
                    check = "Yes"
                    return
                if check_list[nnx][nny] == 0 :
                    if data[nx][ny] == data[nnx][nny] :
                        dfs(nx,ny,nnx,nny,check_list)

check_list = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if not check_list[i][j] :
            first(i,j,check_list)
            k += 1

print(check)