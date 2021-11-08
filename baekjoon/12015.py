## bisect 이용
from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
answer = [0]


for i in range(n):
    if answer[-1] < a[i] :
        answer.append(a[i])
    else :
        answer[bisect_left(answer, a[i])] = a[i]

print(answer)
print(len(answer)-1)


## 이진 탐색 이용
n = int(input())
a = list(map(int, input().split()))
answer = [0]

for i in range(n) :
    if answer[-1] < a[i] :
        answer.append(a[i])
    else :
        start = 0
        end = len(answer) - 1
        while start <= end :
            mid = (start + end) // 2
            if answer[mid] < a[i] :
                start = mid + 1
            elif answer[mid] > a[i] :
                end = mid - 1
            elif answer[mid] == a[i] :
                start = end = mid
        answer[end] = a[i]

print(len(answer)-1)