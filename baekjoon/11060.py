# https://www.acmicpc.net/problem/11060
# 점프 점프

n = int(input())
step = list(map(int, input().split()))
result = [-1] * n
result[0] = 0

def solution(n) :
    for i in range(n):
        if step[i] != 0 and result[i] != -1 :
            for j in range(1, step[i]+1) :
                if i+j > n-1 :
                    break
                if result[i+j] == -1 :
                    result[i+j] = result[i] + 1
                else :
                    result[i+j] = min(result[i+j], result[i]+1)

solution(n)
print(result[n-1])