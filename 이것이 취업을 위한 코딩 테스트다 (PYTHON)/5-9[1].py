# BFS 함수 구현

from collections import deque

def bfs(graph,start,visited) :
    queue = deque([start])
    visited[start] = True
    while queue :
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i] :
                queue.append(i)
                visited[i] = True

# graph 구조는 받아와야 함
n = int(input())
visited = [False] * n
bfs(graph,1,visited)