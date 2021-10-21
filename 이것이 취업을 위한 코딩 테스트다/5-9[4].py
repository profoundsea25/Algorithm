# BFS 함수 구현

from collections import deque

def bfs(graph,start,visited):
    queue = deque([start]) # depue가 뭔지 알아야 queue의 형태를 안다.
    visited[start] = True
    while queue: # 이게 무슨 뜻인지 잘 모름.
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
visited = [False]*n
bfs(graph,1,visited)
