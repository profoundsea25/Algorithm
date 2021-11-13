import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ladders = []
snake_map = [0]*101
for i in range(n):
    ladders.append(list(map(int,input().split())))

ladders.sort(key=lambda x : x[1], reverse=True)

for i in range(m):
    x, y = map(int,input().split())
    snake_map[x] = 1

count = 0
location = 100

def dice (location, target):
    if location <= 7 :
        return 1
    count = 0
    i = 6
    while location > target :
        if location - i <= 1 :
            location = 1
            count += 1
            return count
        elif snake_map[location-i] == 0 :
            location -= i
            count += 1
            i = 6
        elif snake_map[location-i] == 1 :
            i -= 1
    
    return count

for ladder in ladders :
    if location <= 7 :
        break
    if location >= ladder[1] :
        count += dice(location, ladder[1])
        location = ladder[0]
    elif location < ladder[1] :
        continue

count += dice(location, 1)

print(count)


## BFS로 풀기
from collections import deque
def bfs():
    queue = deque([1])
    visited[1] = True
    while queue :
        now = queue.popleft()
        for move in range(1, 7):
            check_move = now + move
            if 0 < check_move <= 100 and not visited[check_move]:
                if check_move in ladder.keys():
                    check_move = ladder[check_move]
                if check_move in snake.keys():
                    check_move = snake[check_move]
                    
                if not visited[check_move]:
                    queue.append(check_move)
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
print(board_cnt[100])