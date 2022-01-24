# https://www.acmicpc.net/problem/13460
# 구슬 탈출 2
# 2022.01.24
from collections import deque

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, -1, 0, 1)
q = deque()

for i in range(n) :
    for j in range(m) :
        if board[i][j] == "R" :
            rx, ry = i, j
        elif board[i][j] == "B" :
            bx, by = i, j
q.append((rx,ry,bx,by,1))
visited[rx][ry][bx][by] = True

def move(x, y, dx, dy) :
    count = 0
    while board[x+dx][y+dy] != "#" and board[x][y] != "O" :
        x += dx
        y += dy
        count += 1
    return x, y, count 

def bfs() :
    while q :
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10 :
            break
        for i in range(4):
            nrx, nry, rcount = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcount = move(bx, by, dx[i], dy[i])
            if board[nbx][nby] == "O" :
                continue

            if board[nrx][nry] == "O" :
                print(depth)
                return

            if nrx == nbx and nry == nby :
                if rcount > bcount :
                    nrx -= dx[i]
                    nry -= dy[i]
                elif rcount < bcount :
                    nbx -= dx[i]
                    nby -= dy[i]


            if not visited[nrx][nry][nbx][nby] :
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx,nry,nbx,nby, depth+1))
    print(-1)

bfs()