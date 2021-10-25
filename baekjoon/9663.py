# DFS 배우고 다시 풀기

# 정답
def check(n):
    for i in range(n):
        if row[n] == row[i] or abs(row[n]-row[i]) == n-i:
            return 0
    return 1
        
def dfs(n):
    global res
    if n == N:
        res += 1
    else:
        for i in range(N):
            row[n] = i
            if check(n):
                dfs(n+1)

N = int(input())
row = [0]*N
res = 0
dfs(0)
print(res)