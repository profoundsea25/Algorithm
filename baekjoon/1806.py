## 시간초과
# n, s = map(int, input().split())
# data = list(map(int, input().split()))

# answer = 20000

# def solution() :
#     global answer
#     for i in range(n):
#         sum_of_data = 0
#         for j in range(i,n):
#             sum_of_data += data[j]
#             if sum_of_data >= s:
#                 length = j - i + 1
#                 answer = min(answer, length)
#                 break
#         if i == 0 and j == n-1 and answer == 20000 :
#             return 0
#     return answer

# print(solution())

## 이진 탐색
# n, s = map(int, input().split())
# data = list(map(int, input().split()))
# answer = 1e9

# def bisect(start, end):
#     global answer
#     if start > end :
#         return
#     mid = (start + end) // 2
    
#     for i in range(n-mid+1):
#         if sum(data[i:i+mid]) >= s :
#             answer = min(answer, mid)
#             return bisect(start, mid-1)
#     else :
#         return bisect(mid+1, end)

# if sum(data) < s :
#     print(0)
# else : 
#     bisect(0, len(data))
#     print(answer)

## 두 포인터?
n, s = map(int, input().split())
data = list(map(int, input().split()))
answer = 1e9

start = 0
end = 0
datasum = data[start]

def find_end(start, end) :
    datasum = data[start]
    while datasum < s :
        end += 1
        if end == n :
            return 0, 0, 0
        datasum += data[end]
    return start, end, datasum

def find_start(start, end, datasum):
    while datasum >= s :
        datasum -= data[start]
        start += 1
    start -= 1
    length = end - start + 1
    return start, length

while start < n and end < n :
    start, end, datasum = find_end(start, end)
    if end == 0 and answer == 1e9 and datasum == 0 :
        print(0)
        exit()
    elif end == 0 and datasum < s :
        break
    else :
        start, length = find_start(start, end, datasum)
        answer = min(answer, length)
        start += 1
        end = start
        datasum = 0

print(answer)

## 좀 더 깔끔한 코드
import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))

left, right, tmp_sum = 0, 0, 0
min_length = sys.maxsize

while True:
   if tmp_sum >= S:
       min_length = min(min_length, right - left)
       tmp_sum -= arr[left]
       left += 1

   elif right == N:
       break

   else:
       tmp_sum += arr[right]
       right += 1

if min_length == sys.maxsize:
   print(0)
else:
   print(min_length)