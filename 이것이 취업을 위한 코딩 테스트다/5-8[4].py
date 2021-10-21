# DFS 함수 구현

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]: # visited[i]가 False면,
            # visited[i] = True -> 이미 dfs안에 있기 때문에 안써도 OK
            dfs(graph, i, visited)

n = int(input()) # 노드 개수 n 받기
graph = []
for i in range(n): # n개의 노드 연결 리스트 받기
    graph.append(list(map(int, input())))
visited = [False] * n
dfs(graph,1,visited)
