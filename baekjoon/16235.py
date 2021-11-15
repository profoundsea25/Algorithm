from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

trees = [[deque([]) for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

land = [[5 for _ in range(n)] for _ in range(n)]

def spring_and_summer() :
    global trees
    global land
    for i in range(n):
        for j in range(n):
            if trees[i][j] :
                for x in range(len(trees[i][j])) :
                    if land[i][j] - trees[i][j][x] >= 0 :
                        land[i][j] = land[i][j] - trees[i][j][x]
                        trees[i][j][x] += 1
                    else :
                        for _ in range(x, len(trees[i][j])) :
                            land[i][j] += trees[i][j].pop() // 2
                        break

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def fall_and_winter() :
    global trees
    global land
    for i in range(n):
        for j in range(n):
            if trees[i][j] :
                for tree in trees[i][j] :
                    if tree % 5 == 0 :
                        for z in range(8):
                            ni = i + dx[z]
                            nj = j + dy[z]
                            if ni < n and nj < n and ni >= 0 and nj >=0 :
                                trees[ni][nj].appendleft(1)
            # winter
            land[i][j] += a[i][j]

for i in range(k):
    spring_and_summer()
    fall_and_winter()

answer = 0
for i in range(n):
    for j in range(n):
        if trees[i][j] :
            answer += len(trees[i][j])

print(answer)