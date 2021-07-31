# DFS 함수 구현

def dfs(graph,v,visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

# graph 구조는 받아와야 함
graph = []
n = int(input())
visited = [False] * n
dfs(graph,1,visited)