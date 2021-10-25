import sys
input = sys.stdin.readline

n = int(input())

answer = [0] * n
step_score = [0] * n
for i in range(n):
    x = int(input())
    step_score[i] = x

    if i == 0 :
        answer[i] = x
    elif i == 1 :
        answer[i] = step_score[0] + x
    elif i == 2 :
        answer[i] = max(step_score[0], step_score[1]) + x
    else :
        answer[i] = max(answer[i-3]+step_score[i-1], answer[i-2]) + x

result = answer[i]
print(result)
