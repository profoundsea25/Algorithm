# BFS 구현 [3]

from collections import deque
def bfs(graph,start,visited):
    queue = deque([start]) # deque 함수가 무엇?
    visited[start] = True
    while queue : # while queue? True인건 알겠다만...
        v = queue.popleft()
        print(v, end=' ') # popleft가 삭제 + 뽑기
        for i in graph[v]: # graph[v]의 1번 째 원소부터
            if not visited[i]: # visited[1]이 False면,
                queue.append(i) # queue 맨 뒤에 i 넣고
                visited[i] = True # 방문 처리

graph = []
n = int(input())
visited = [False] * n # n은 graph의 행의 개수(노드의 개수)
bfs(graph,1,visited)