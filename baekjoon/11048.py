## DFS
# import sys
# sys.setrecursionlimit(10000)

# n, m = map(int, input().split())
# data = []
# for i in range(n):
#     data.append(list(map(int, input().split())))

# dx = [1,0,1]
# dy = [0,1,1]

# answer = 0
# def dfs(x, y, candy) :
#     global answer
#     candy += data[x][y]
#     if x == n-1 and y == m-1 :
#         if answer < candy :
#             answer = candy
#         return
    
#     for i in range(3):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if nx < n and ny < m :
#             dfs(nx, ny, candy)

# dfs(0,0,0)
# print(answer)


## DP
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

for i in range(1,m):
    data[0][i] += data[0][i-1]
for j in range(1,n):
    data[j][0] += data[j-1][0]

for i in range(1,n):
    for j in range(1,m):
        data[i][j] += max(data[i-1][j-1], data[i][j-1], data[i-1][j])

print(data[n-1][m-1])