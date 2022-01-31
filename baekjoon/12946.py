# https://www.acmicpc.net/problem/12946
# 육각 보드
# 2022.01.31

import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
color = [[-1]*n for _ in range(n)]
dx, dy = (-1,-1,0,1,1,0), (0,1,1,0,-1,-1)
answer = 0

def dfs(x, y, c) :
    global answer
    answer = max(answer, 1)
    color[x][y] = c
    for i in range(6) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == "X" :
            if color[nx][ny] == -1 :
                answer = max(answer, 2)
                dfs(nx, ny, 1 - c)
            if color[nx][ny] == c :
                print(3)
                exit()
            
for i in range(n) :
    for j in range(n) :
        if graph[i][j] == "X" and color[i][j] == -1:
            dfs(i,j,0)

print(answer)