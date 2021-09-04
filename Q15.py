# Q 15 특정 거리의 도시 찾기, p.339 / 530
from collections import deque

n, m, k, x = map(int, input().split())
road = [[] for _ in range(n)]
visited = [-1] * n
for i in range(m) :
    a, b = map(int, input().split())
    road[a-1].append(b)

queue = deque([x-1])
visited[x-1] = 0
while queue :
    v = queue.popleft()
    for i in road[v]:
        if visited[i-1] == -1 :
            queue.append(i-1)
            visited[i-1] = visited[v] + 1
check = 0
for i in range(len(visited)):
    if visited[i] == k :
        print(i+1)
        check = 1
if check == 0 :
    print(-1)
