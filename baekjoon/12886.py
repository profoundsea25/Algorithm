# https://www.acmicpc.net/problem/12886
# 돌 그룹
# 2022.03.01

# import copy

# number_set = list(map(int, input().split()))
# number_set.sort()
# result_list = []
# result_list.append(copy.deepcopy(number_set))


# while True :
#     x = number_set.pop(0)
#     y = number_set.pop(1)

#     if x == y :
#         print(1)
#         exit()

#     y -= x
#     x += x
    
#     number_set.append(x)
#     number_set.append(y)
#     number_set.sort()

#     check = copy.deepcopy(number_set)
#     print(check)
#     print(result_list)
#     if check in result_list :
#         print(0)
#         exit()
#     result_list.append(check)


# 정답
from collections import deque

a, b, c = map(int, input().split())
t = a + b + c
check = [[False]*t for _ in range(t)]

def bfs(init_x, init_y) :
    q = deque()
    q.append((init_x,init_y))
    check[init_x][init_y] = True
    while q:
        x, y = q.popleft()
        z = t-x-y
        if x == y == z :
            print(1)
            return
        for i, j in (x,y), (x,z), (y,z) :
            if i < j :
                j -= i
                i += i
            elif i > j :
                i -= j
                j += j
            else :
                continue
            k = t-i-j
            min_n = min(i,j,k)
            max_n = max(i,j,k)
            if not check[min_n][max_n]:
                q.append((min_n,max_n))
                check[min_n][max_n] = True
    print(0)

if t % 3 :
    print(0)
else :
    bfs(min(a,b,c),max(a,b,c))