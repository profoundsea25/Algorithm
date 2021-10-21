from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque() ## queue를 deque로 선언
    queue.append((x,y)) ## queue에 x,y 대입
    while queue: ## queue 가 빌때까지
        x,y = queue.popleft() ## x,y 를 방문했으니 꺼낸다.
        for i in range(4): ## 방향을 움직이고
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: #예외처리 1
                continue
            if graph[nx][ny] == 0 : # 예외처리 2
                continue
            if graph[nx][ny] == 1 : # 가야할 길이면
                graph[nx][ny] = graph[x][y] + 1 # 숫자를 추가
                queue.append((nx,ny)) # 그 다음 x,y 좌표를 입력
    return graph[n-1][m-1] # 0,0부터 시작하므로 n-1,m-1 출력

print(bfs(0,0))