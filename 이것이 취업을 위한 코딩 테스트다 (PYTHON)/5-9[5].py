# BFS 함수 구현
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start]) # 여전히 deque에 대한 공부 필요
    visited[start] = True 
    while queue: # 현재 queue는 deque함수인데..
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]: # 여기서부터는 그림으로 생각해보자.
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
visited = [False] * n
bfs(graph, 1, visited)