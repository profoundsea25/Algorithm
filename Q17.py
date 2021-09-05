# Q 17 경쟁적 전염, p.344 / 535
# 시간 초과

#n = 3; k = 3; graph = [[1,0,2],[0,0,0],[3,0,0]]; s = 2; x = 3; y = 2; virus = [[[0,0]],[[0,2]],[[2,0]]]
#n = 4; k = 3; graph = [[1,0,0,2],[0,0,0,0],[0,0,0,0],[3,0,0,0]]; s = 3; x = 4; y = 3; virus = [[[0,0]],[[0,3]],[[3,0]]]
#n = 3; k = 3; graph = [[1,0,2],[0,0,0],[3,0,0]]; s = 1; x = 2; y = 2; virus = [[[0,0]],[[0,2]],[[2,0]]]
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = []
virus = [[] for _ in range(k)]
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0 :
            virus[graph[i][j]-1].append((i, j))
s, x, y = map(int, input().split())

def dfs(x ,y, k, graph) :
    if x-1 >= 0 and graph[x-1][y] == 0 :
        graph[x-1][y] = k
        virus[k-1].append((x-1,y))
    if y+1 < n and graph[x][y+1] == 0 :
        graph[x][y+1] = k
        virus[k-1].append((x,y+1))
    if x+1 < n and graph[x+1][y] == 0 :
        graph[x+1][y] = k
        virus[k-1].append((x+1,y))
    if y-1 >= 0 and graph[x][y-1] == 0 :
        graph[x][y-1] = k
        virus[k-1].append((x,y-1))
    return True

time = 0
check = [[0]*n for _ in range(n)]

while(time < s) :
    for i in range(len(virus)) :
        for j in range(len(virus[i])):
            if check[virus[i][j][0]][virus[i][j][1]] == 0:
                dfs(virus[i][j][0],virus[i][j][1],i+1,graph)
                check[virus[i][j][0]][virus[i][j][1]] = 1
    time += 1

print(graph[x-1][y-1])