# DFS 함수 구현 3

def dfs(graph,v,visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

graph = []
n = int(input())
visited = [False] * n # v가 아니라 n
dfs(graph,1,visited) # v가 아니라 1부터 시작