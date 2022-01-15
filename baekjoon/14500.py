# https://www.acmicpc.net/problem/14500
# 테트로미노
# 2022.01.16 01:48 ~ 2:48

n, m = map(int, input().split())
nums = []
for _ in range(n):
    nums.append([0,0,0] + list(map(int, input().split())) + [0,0,0])

data = [[0]*(m+6) for _ in range(3)]
data = data + nums
data += [[0]*(m+6) for _ in range(3)]

def solution(i,j) :
    tetromino = []
    # 유형 2 - 1개
    tetromino.append(sum([data[i][j], data[i][j+1], data[i+1][j], data[i+1][j+1]]))

    # 유형 1 - 2개
    tetromino.append(sum([data[i][j], data[i][j+1], data[i][j+2], data[i][j+3]]))
    tetromino.append(sum([data[i][j], data[i+1][j], data[i+2][j], data[i+3][j]]))

    # 유형 5 - 4개
    tetromino.append(sum([data[i][j], data[i][j+1], data[i][j+2], data[i+1][j+1]]))
    tetromino.append(sum([data[i][j], data[i][j+1], data[i][j+2], data[i-1][j+1]]))
    tetromino.append(sum([data[i][j], data[i+1][j], data[i+1][j+1], data[i+2][j]]))
    tetromino.append(sum([data[i][j], data[i+1][j], data[i+1][j-1], data[i+2][j]]))

    # 유형 4 - 4개
    tetromino.append(sum([data[i][j], data[i][j+1], data[i+1][j+1], data[i+1][j+2]]))
    tetromino.append(sum([data[i][j], data[i][j+1], data[i-1][j+1], data[i-1][j+2]]))
    tetromino.append(sum([data[i][j], data[i+1][j], data[i+1][j+1], data[i+2][j+1]]))
    tetromino.append(sum([data[i][j], data[i+1][j], data[i+1][j-1], data[i+2][j-1]]))

    # 유형 3 - 8개
    tetromino.append(sum([data[i][j], data[i][j+1], data[i][j+2], data[i+1][j+2]]))
    tetromino.append(sum([data[i][j], data[i][j+1], data[i][j+2], data[i-1][j+2]]))
    tetromino.append(sum([data[i][j], data[i][j-1], data[i][j-2], data[i+1][j-2]]))
    tetromino.append(sum([data[i][j], data[i][j-1], data[i][j-2], data[i-1][j-2]]))
    tetromino.append(sum([data[i][j], data[i+1][j], data[i+2][j], data[i+2][j+1]]))
    tetromino.append(sum([data[i][j], data[i+1][j], data[i+2][j], data[i+2][j-1]]))
    tetromino.append(sum([data[i][j], data[i-1][j], data[i-2][j], data[i-2][j+1]]))
    tetromino.append(sum([data[i][j], data[i-1][j], data[i-2][j], data[i-2][j-1]]))

    return max(tetromino)

result = 0
for i in range(3,n+3) :
    for j in range(3,m+3) :
        result = max(result, solution(i,j))

print(result)