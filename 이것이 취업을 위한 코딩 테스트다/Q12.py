# Q 12 기둥과 보 설치, p.329 / 525

# [x좌표, y좌표, 0기둥, 0삭제]
# [x좌표, y좌표, 1보  , 1설치]
def solution(n, build_frame) :
    result = []
    map = [[-1] * (n+1) for _ in range(n+1)]
    for x in build_frame :
        # 기둥 설치
        if x[2] == 0 and x[3] == 1 :
            if x[1] == 0 or map[x[0]-1][x[1]] == 1 or map[x[0]][x[1]-1] == 0 :
                map[x[0]][x[1]] = 0
        # 보 설치
        elif x[2] == 1 and x[3] == 1 :
            if x[1] != 0 and map[x[0]][x[1]-1] == 0 or map[x[0]+1][x[1]-1] == 0 or (map[x[0]-1][x[1]] == 1 and map[x[0]+1][x[1]] == 1) :
                map[x[0]][x[1]] = 1
        # 기둥 삭제
        elif x[2] == 0 and x[3] == 0 :
            if (map[x[0]-1][x[1]+1] == 1 and map[x[0]][x[1]+1] == 1 and (map[x[0]+1][x[1]] == 0 or map[x[0]+1][x[1]+1] == 1)) or map[x[0]][x[1]+1] == -1 :
                map[x[0]][x[1]] = -1
        # 보 삭제
        else :
            if (map[x[0]-1][x[1]-1] == 0 and map[x[0]+1][x[1]] != 1) or (map[x[0]-1][x[1]-1] == 0 and map[x[0]+1][x[1]-1] == 0) :
                map[x[0]][x[1]] = -1

    for i in range(n+1) :
        for j in range(n+1) :
            if map[i][j] == 0 :
                result.append([i,j,0])
            elif map[i][j] == 1 :
                result.append([i,j,1])
    return result
    

n = 5
#build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
result = solution(n, build_frame)
print(result)