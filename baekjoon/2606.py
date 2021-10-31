n = int(input())
m = int(input())

computer = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    computer[x].append(y)
    computer[y].append(x)

visited = [False]*(n+1)
def bfs(number) :
    visited[number] = True
    for i in computer[number]:
        if visited[i] == False :
            bfs(i)

bfs(1)

print(visited.count(True)-1)