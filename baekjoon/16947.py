import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# dfs result 설명
# -2 : 사이클을 찾았으나 해당 정점은 사이클에 포함되지 않음
# -1 : 사이클을 찾지 못한 경우
# 0 이상 : 사이클을 찾았으며 시작 정점의 번호가 저장됨.
def dfs(here, start): # (현재 위치, 시작 위치), 사이클 구하기
    if check[here] == 1 : # 이미 방문한 적 있는 노드면 return (사이클을 찾았다)
        return here 
    check[here] = 1 # 방문 체크

    for next in graph[here] : # 현재 위치에서 연결된 노드들(next)
        if next == start : # 갈 곳의 노드가 시작점 노드와 같으면 pass
            continue
        result = dfs(next, here)
        if result == -2 :
            return -2
        if result >= 0 : # 0 이상일 경우 사이클에 포함되는 정점
            check[here] = 2 # 해당 정점은 사이클에 포함되는 정점임을 기록한다.
            return result if here != result else -2 # 사이클 시작점부터는 -2로 기록.
    
    return -1

def bfs() :
    q = []
    for i in range(n):
        if check[i] == 2:
            q.append(i) # 사이클에 포함될 경우 거리 0
        else :
            dist[i] = -1 # 사이클에 포함 안 될 경우 -1로 초기화

    while q :
        tmp = []

        for here in q :
            for next in graph[here] :
                if dist[next] == -1 : 
                    # 아직 방문하지 않은 노드인 경우
                    dist[next] = dist[here] + 1 # 거리를 늘려준다. 
                    tmp.append(next) # 해당 정점을 queue에 넣고
        q = tmp

n = int(input())
graph = [[] for _ in range(n)] # 노드 리스트
check = [0]*n # 방문 여부
dist = [-1]*n # 거리

for _ in range(n):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

dfs(0,-1)
bfs()
print(dist)