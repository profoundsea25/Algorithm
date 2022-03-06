# https://www.acmicpc.net/problem/17143
# 낚시왕
# 2022.03.06

import copy
import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
sharks = [] # 모든 상어의 정보
shark_list = set() # 현재 생존한 상어 리스트
new_shark_list = set() # 다음 시간에 생존하는 상어 리스트
table = [[-1]*C for _ in range(R)] # 한 칸에 상어가 두 마리 이상인지 판별하기 위한 이중 리스트
answer = 0

closest = R+1
shark_index_to_remove = M

# 처음에 정보를 받을 때 편의상 첫 상어를 잡음
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks.append([r,c,s,d,z,i]) # 상어를 판별하기 위한 리스트, 인덱스(i) = 상어 번호
    shark_list.add(i)

    if c == 1 and r < closest :
        closest = r
        shark_index_to_remove = i

if shark_index_to_remove != M :
    shark_list.remove(shark_index_to_remove)
    answer += sharks[shark_index_to_remove][4]


def solution(second) :
    global shark_list, new_shark_list, table, closest, shark_index_to_remove, answer
    table = [[-1]*C for _ in range(R)]
    new_shark_list = copy.deepcopy(shark_list)
    closest = R+1 ## chck point
    shark_index_to_remove = M

    for n in shark_list :
        # 상어 이동 & 한 칸에 두 마리 이상일 경우 한 마리로 제거
        sharks[n][0], sharks[n][1], sharks[n][3] = move_shark(sharks[n], second) ## chck point

    if shark_index_to_remove != M :
        new_shark_list.remove(shark_index_to_remove)
        answer += sharks[shark_index_to_remove][4]

    shark_list = copy.deepcopy(new_shark_list)

def move_shark(shark, second) :
    global table, new_shark_list, closest, shark_index_to_remove
    r,c,s,d,z,i = shark

    # 상어 이동
    while s > 0 :
        if d == 1 :
            if r != 1 :
                r -= 1
            else :
                d = 2
                r += 1
        elif d == 2 : ## chck point
            if r != R :
                r += 1
            else :
                d = 1
                r -= 1
        elif d == 3 : ## chck point
            if c != C :
                c += 1
            else :
                d = 4
                c -= 1
        elif d == 4 : ## chck point
            if c != 1 :
                c -= 1
            else :
                d = 3
                c += 1

        s -= 1
    
    # 한 칸에 두 마리 이상일 경우
    if table[r-1][c-1] == -1 :
        table[r-1][c-1] = i
    elif table[r-1][c-1] != -1 :
        if z > sharks[table[r-1][c-1]][4] :
            new_shark_list.remove(table[r-1][c-1])
            table[r-1][c-1] = i
        else :
            new_shark_list.remove(i) ## chck point

    # 가장 가까운 상어 제거를 위한 변수
    if c == second and r <= closest :
        closest = r
        if i in new_shark_list :
            shark_index_to_remove = i
        else :
            shark_index_to_remove = table[r-1][c-1] ## chck point

    return r, c, d

for second in range(2,C+1): ## chck point
    solution(second)

print(answer)


## 정답
import sys
input = sys.stdin.readline
def shMove():
    temp = [[0] * C for i in range(R)]
    for i in range(R):
        for j in range(C):
            if g[i][j] != 0:
                x, y, s, d, z = i, j, g[i][j][0], g[i][j][1], g[i][j][2]
                while s > 0:
                    x += dx[d]
                    y += dy[d]
                    if 0 <= x < R and 0 <= y < C:
                        s -= 1
                    else:
                        x -= dx[d]
                        y -= dy[d]
                        if d == 0: d = 1
                        elif d == 1: d = 0
                        elif d == 2: d = 3
                        elif d == 3: d = 2
                if temp[x][y] == 0:
                    temp[x][y] = [g[i][j][0], d, z]
                else:
                    if temp[x][y][2] < z:
                        temp[x][y] = [g[i][j][0], d, z]
    return temp
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
R, C, m = map(int, input().split())
g = [[0] * C for i in range(R)]
for i in range(1, m + 1):
    r, c, s, d, z = map(int, input().split())
    g[r - 1][c - 1] = [s, d - 1, z]
result = 0
for i in range(C):
    for j in range(R):
        if g[j][i] != 0:
            result += g[j][i][2]
            g[j][i] = 0
            break
    g = shMove()
print(result)