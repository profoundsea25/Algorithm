n, m = map(int, input().split())
trees = list(map(int,input().split()))

start = 0
end = max(trees)
answer = 0
while start <= end :                # start <= end는 이진 탐색의 조건이다.
    mid = (start + end) // 2

    log = 0
    for tree in trees :
        if tree > mid :             # 조건을 왜 까먹어
            log += tree - mid
    
    if log >= m :
        answer = mid                # 정답을 찍어내는 타이밍 중요
        start = mid + 1
    elif log < m :
        end = mid - 1

print(answer)

# 안 보고 짜기
n, m = map(int,input().split())
trees = list(map(int,input().split()))

start, end, answer = 0, max(trees), 0

while start <= end :
    mid = (start + end) // 2

    log = 0
    for tree in trees :
        if tree > mid :
            log += tree - mid

    if log >= m :
        answer = mid
        start = mid + 1
    else :
        end = mid - 1

print(answer)