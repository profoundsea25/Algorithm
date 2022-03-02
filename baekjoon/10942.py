# https://www.acmicpc.net/problem/10942
# 팰린드롬?
# 2022.03.02

# ## 시간 초과
# import sys
# input = sys.stdin.readline

# def solution(x, y) :
#     target = numbers[x:(y+1)]

#     if x == y :
#         return print(1)
#     elif (x - y) % 2 == 0 :
#         for i in range((y+1-x)//2):
#             if not target[i] == target[y-x-i] :
#                 return print(0)
#     elif (x - y) % 2 == 1 :
#         for i in range((y+1-x)//2 - 1) :
#             if not target[i] == target[y-x-i] :
#                 return print(0)
#     return print(1)

# n = int(input())
# numbers = [0]
# numbers += list(map(int,input().split()))
# numbers.append(0)
# m = int(input())
# for i in range(m) :
#     x, y = map(int,input().split())
#     solution(x, y)



# ## 오답
# import sys
# input = sys.stdin.readline

# def solution(x, y) :
#     global result_set
#     target = numbers[x:(y+1)]

#     if x == y :
#         result_set.add(x)
#         return print(1)
#     elif (x+y)/2 in result_set :
#         return print(1)
#     elif (x - y) % 2 == 0 :
#         for i in range((y+1-x)//2):
#             if not target[i] == target[y-x-i] :
#                 return print(0)
#     elif (x - y) % 2 == 1 :
#         for i in range((y+1-x)//2 - 1) :
#             if not target[i] == target[y-x-i] :
#                 return print(0)
    
#     result_set.add((y+x)/2)
#     return print(1)

# n = int(input())
# numbers = [0]
# numbers += list(map(int,input().split()))
# numbers.append(0)
# result_set = set()
# m = int(input())
# for i in range(m) :
#     x, y = map(int,input().split())
#     solution(x, y)


##
import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int,input().split()))
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if numbers[i] == numbers[i+1] :
        dp[i][i+1] = 1

for j in range(2, n):
    for i in range(n-j):
        if numbers[i] == numbers[i+j] and dp[i+1][i+j-1] == 1 :
            dp[i][i+j] = 1

m = int(input())
for _ in range(m) :
    x, y = map(int,input().split())
    print(dp[x-1][y-1])    