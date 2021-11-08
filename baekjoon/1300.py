## Try 1. 메모리 초과
# n = int(input())
# k = int(input())

# answer = [0 for _ in range(1+n**2)]

# for i in range(n) :
#     for j in range(n):
#         answer[(i+1)*(j+1)] += 1

# count = 0
# for i in range(len(answer)):
#     count += answer[i]
#     if count >= k :
#         print(i)
#         break


### Try 2. 메모리 초과
# n = int(input())
# k = int(input())

# answer = []
# for i in range(n):
#     for j in range(i+1, n):
#         answer.append((i+1)*(j+1))

# answer.sort()

# count = 0
# j = 1
# for i in range(len(answer)):
#     if answer[i] < (j)**2 :
#         count += 2
#     else :
#         count += 3
#         j += 1
#     if count > k :
#         print(answer[i])
#         break


### Try 3. 이분 탐색
n = int(input())
k = int(input())

start = 1
end = k 

while start <= end :
    mid = (start + end) // 2

    check = 0
    for i in range(1, n+1) :
        check += min(mid//i, n)
    
    if check < k :
        start = mid + 1
    else :
        end = mid - 1
        answer = mid

print(answer)