from itertools import combinations

n, s = map(int, input().split())
data = list(map(int,input().split()))

count = 0

for i in range(1,n+1):
    answer = list(combinations(data,i))
    for j in answer:
        if s == sum(j):
            count += 1

print(count)

## dfs 로 구현하기
def dfs(idx, sum):
    global cnt
    if idx >= n:
        return
    sum += s_[idx]
    if sum == s:
        cnt += 1
    dfs(idx + 1, sum - s_[idx])
    dfs(idx + 1, sum)
n, s = map(int, input().split())
s_ = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)