import sys
input = sys.stdin.readline

n = int(input())
costs = []
for i in range(n):
    costs.append(list(map(int, input().split())))

result = sys.maxsize
count = 0

def dfs(i, p, cost) :
    global result
    if i == 0 :
        for k in range(3):
            check = cost + costs[i][k]
            dfs(i+1, k, check)
    elif 0 < i < n :
        for k in range(3):
            if k == p :
                pass
            else :
                check = cost + costs[i][k]
                dfs(i+1, k, check)
    elif i == n :
        result = min(cost, result)
        return

dfs(0,0,0)
print(result)


# 정답 (훨씬 간단...) 일종의 메모이제이션?
n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
for i in range(1, len(p)):
    p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))