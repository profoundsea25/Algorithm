import sys
input = sys.stdin.readline
limit_number = 5000
sys.setrecursionlimit(5000)

t = int(input())

def bfs(y,x) :
    global data
    data[y][x] = 2
    if y > 0 and data[y-1][x] == 1 :
        bfs(y-1,x)
    if y < n-1 and data[y+1][x] == 1 :
        bfs(y+1,x)
    if x > 0 and data[y][x-1] == 1 :
        bfs(y,x-1)
    if x < m-1 and data[y][x+1] == 1 :
        bfs(y,x+1)

for i in range(t):
    m, n, k = map(int, input().split())
    data = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        data[y][x] = 1
    count = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1 :
                bfs(i,j)
                count += 1
    print(count)


# 다른 풀이
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

t = int(input())

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

for i in range(t):
    cnt = 0
    n, m, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)