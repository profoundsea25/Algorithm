# Q 16 연구소, p.341 / 531
from itertools import combinations

n, m = map(int, input().split())
graph = []
loc0 = []
locv = []
for i in range(n) :
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 0:
            loc0.append((i,j))
        elif graph[i][j] == 2:
            locv.append((i,j))

wallcomb = list(combinations(loc0, 3))
i = 0
safe = 0

def dfs(x,y,test):
    if test[x][y] == 2 :
        if x-1 > -1 and test[x-1][y] == 0 :
            test[x-1][y] = 2
            dfs(x-1,y,test)
        if y-1 > -1 and test[x][y-1] == 0 :
            test[x][y-1] = 2
            dfs(x,y-1,test)
        if x+1 < n and test[x+1][y] == 0 :
            test[x+1][y] = 2
            dfs(x+1,y,test)
        if y+1 < m and test[x][y+1] == 0 :
            test[x][y+1] = 2
            dfs(x,y+1,test)
        return True
    return False

test = [[0]*m for _ in range(n)]

while(i < len(wallcomb)):
    for l in range(n):
        for z in range(m):
            test[l][z] = graph[l][z]
    count = 0
    test[wallcomb[i][0][0]][wallcomb[i][0][1]] = 1
    test[wallcomb[i][1][0]][wallcomb[i][1][1]] = 1
    test[wallcomb[i][2][0]][wallcomb[i][2][1]] = 1
    for v in locv:
            dfs(v[0],v[1],test)
    for j in range(n):
        for k in range(m):
            if test[j][k] == 0:
                count += 1
    safe = max(safe, count)
    i += 1

print(safe)