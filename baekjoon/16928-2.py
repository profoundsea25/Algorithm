# from collections import deque
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# data = [0] * 101
# visited = [False] * 101

# ladder = dict()
# snake = dict()

# for _ in range(n):
#     x, y = map(int, input().split())
#     ladder[x] = y
# for _ in range(m):
#     x, y = map(int, input().split())
#     snake[x] = y

# def bfs():
#     q = deque([1])
#     visited[1] = True
#     while q :
#         now = q.popleft()
#         for move in range(1,7):
#             check_move = now + move
#             if 0 < check_move <= 100 and not visited[check_move]:
#                 if check_move in ladder.keys():
#                     check_move = ladder[check_move]
#                 if check_move in snake.keys():
#                     check_move = snake[check_move]
                
#                 if not visited[check_move]:
#                     q.append(check_move)
#                     visited[check_move] = True
#                     data[check_move] = data[now] + 1

# bfs()
# print(data[-1])


## 안보고 풀기
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [0]*101
visited = [False]*101
ladder = dict()
snake = dict()

for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    x, y = map(int, input().split())
    ladder[x] = y

def bfs() :
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
                    data[check_move] += data[now] + 1

bfs()
print(data[-1])