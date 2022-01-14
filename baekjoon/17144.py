# https://www.acmicpc.net/problem/17144
# 미세먼지 안녕!
# 2022.01.14 17:20 ~ 19:30

import copy

r, c, t = map(int, input().split())
graph = []
cleaner_location = []
for i in range(r):
    graph.append(list(map(int, input().split())))
    if graph[i][0] == -1 :
        cleaner_location.append(i)

spread_map = [[0]*c for _ in range(r)]
spread_map[cleaner_location[0]][0] = -1
spread_map[cleaner_location[1]][0] = -1

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def spread() :
    for i in range(r):
        for j in range(c) :
            if graph[i][j] > 0 :
                count = 0
                for k in range(4) :
                    ni = i + dx[k]
                    nj = j + dy[k]

                    if 0 <= ni < r and 0 <= nj < c and graph[ni][nj] != -1 :
                        spread_map[ni][nj] += graph[i][j] // 5
                        count += graph[i][j] // 5
                spread_map[i][j] += graph[i][j] - count

def clean_up() :
    i = cleaner_location[0]
    cleaned_map[i] = [-1, 0] + spread_map[i][1:-1]    
    cleaned_map[0] = spread_map[0][1:] + [0]
    while(i-1 >= 0) :
        cleaned_map[i-1][-1] = spread_map[i][-1]
        cleaned_map[cleaner_location[0]-i+1][0] = spread_map[cleaner_location[0]-i][0]
        i -= 1
    cleaned_map[cleaner_location[0]][0] = -1

def clean_down() :
    i = cleaner_location[1]
    cleaned_map[i] = [-1, 0] + spread_map[i][1:-1]
    cleaned_map[r-1] = spread_map[r-1][1:] + [0]
    while (i+1 < r) :
        cleaned_map[i+1][-1] = spread_map[i][-1]
        cleaned_map[r-1+cleaner_location[1]-i-1][0] = spread_map[r-1+cleaner_location[1]-i][0]
        i += 1
    cleaned_map[cleaner_location[1]][0] = -1

for _ in range(t) :
    spread()
    cleaned_map = copy.deepcopy(spread_map)
    clean_up()
    clean_down()
    graph = copy.deepcopy(cleaned_map)
    spread_map = [[0]*c for _ in range(r)]
    spread_map[cleaner_location[0]][0] = -1
    spread_map[cleaner_location[1]][0] = -1

result = 2
for i in range(r) :
    result += sum(cleaned_map[i])
print(result)