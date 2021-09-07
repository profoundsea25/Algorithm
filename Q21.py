# Q 21 인구이동, p.353 / 542
import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

n, L, R = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))
count = 0

is_open = [[0] * n for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def dfs(x,y,graph):
    global z
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if abs(graph[x][y]-graph[nx][ny]) >= L and abs(graph[x][y]-graph[nx][ny]) <= R :
                if is_open[x][y] == 0 or is_open[nx][ny] == 0:
                    is_open[x][y] = z
                    is_open[nx][ny] = z
                    dfs(nx,ny,graph)

while(True):
    is_open = [[0] * n for _ in range(n)]
    z = 1
    for x in range(n):
        for y in range(n):
            if is_open[x][y] == 0 :
                dfs(x,y,A)
                z += 1
    if is_open == [[0] * n for _ in range(n)] :
        break
    zset = []
    for i in range(n):
        for j in range(n):
            if is_open[i][j] != 0:
                if is_open[i][j] not in zset :
                    zset.append(is_open[i][j])
    for z in zset :
        opend = []
        sum = 0
        div = 0
        for w in range(n):
            for q in range(n):
                if is_open[w][q] == z :
                    opend.append((w,q))
                    sum += A[w][q]
                    div += 1
        for w, q in opend :
            A[w][q] = sum // div
    count += 1

print(count)