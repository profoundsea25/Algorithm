# <3> 음료수얼려먹기 [1]
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x,y) :
    if x <= -1 or x >= n or y <= -1 or y >= m : # 예외처리
        return False
    if graph[x][y] == 0 : # 현재 노드 방문처리
        graph[x][y] = 1
        dfs(x-1,y) # 좌하우상 위치 모두 재귀적으로 호출 
        dfs(x,y-1) # 결과적으로 return하는 값은
        dfs(x+1,y) # True 아니면 False
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True :
            result += 1

print(result)