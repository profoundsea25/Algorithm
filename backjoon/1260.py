from collections import deque

n, m, v = map(int,input().split())
graph = {}
for i in range(1,n+1):
    graph[i] = []

for i in range(m):
    node_1, node_2 = map(int,input().split())
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)

visited = []
def dfs(graph, v, visited): # dfs는 재귀 혹은 stack으로 풀 수 있음
    visited.append(v)
    graph[v].sort()
    for i in graph[v] :
        if i not in visited :
            visited = dfs(graph,i,visited)
    return visited

visited = dfs(graph,v,visited)
for i in visited :
    print(i, end=' ')
print()

visited = []
def bfs(graph, v, visited): # bfs는 deque로 풀 수 있음
    queue = deque([])
    queue.append(v)

    while queue :
        now = queue.popleft()
        graph[now].sort()
        visited.append(now)
        for i in graph[now]:
            if i not in queue and i not in visited :
                queue.append(i)

    return visited

visited = bfs(graph,v,visited)
for i in visited:
    print(i, end=" ")