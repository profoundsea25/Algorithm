# BFS로 풀기
from collections import deque
def bfs () :
    q = deque([1])
    visited[1] = True
    while q :
        now = q.popleft()
        for move in range(1,7):
            check_move = now + move
            if 0 < check_move <= 100 and not visited[check_move]:
                if check_move in ladder.keys():
                    check_move = ladder[check_move]
                if check_move in snake.keys():
                    check_move = snake[check_move]
                
                if not visited[check_move]:
                    q.append(check_move)
                    visited[check_move] = True
                    board_cnt[check_move] = board_cnt[now] + 1

n, m = map(int, input().split())
board_cnt = [0]*101
visited = [False]*101

snake = dict()
ladder = dict()
for _ in range(n):
    i, j = map(int, input().split())
    ladder[i] = j
for _ in range(m):
    i, j = map(int, input().split())
    snake[i] = j

bfs()
print(board_cnt[-1])


## 안보고 짜기 BFS
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board_cnt = [0]*101
visited = [False]*101

ladder = dict()
snake = dict()
for _ in range(n):
    i, j = map(int, input().split())
    ladder[i] = j
for _ in range(m):
    i, j = map(int, input().split())
    snake[i] = j

def bfs() :
    q = deque([1])
    visited[1] = True
    while q :
        now = q.popleft()
        for move in range(1,7):
            check_move = now + move
            if 0 < check_move <= 100 and not visited[check_move] :
                if check_move in ladder.keys():
                    check_move = ladder[check_move]
                if check_move in snake.keys():
                    check_move = snake[check_move]

                if not visited[check_move]:
                    q.append(check_move)
                    visited[check_move] = True
                    board_cnt[check_move] += board_cnt[now] + 1

bfs()
print(board_cnt[-1])









