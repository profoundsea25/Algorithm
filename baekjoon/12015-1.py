# bisect 이용
from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))

answer = [0]
for i in range(n):
    if a[i] > answer[-1] :
        answer.append(a[i])
    else :
        answer[bisect_left(answer,a[i])] = a[i]

print(len(answer)-1)