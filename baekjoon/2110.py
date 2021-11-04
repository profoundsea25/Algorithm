## 메모리 초과
# from itertools import combinations

# import sys
# input = sys.stdin.readline

# n, c = map(int, input().split())
# house = []
# for i in range(n) :
#     house.append(int(input()))

# combs = list(combinations(house, c))
# result = []

# for i in combs:
#     for_abs = list(combinations(i, 2))
#     combs_max = 0
#     for j in for_abs :
#         diff = abs(j[0]-j[1])
#         combs_max = max(diff, combs_max)
#     result.append(combs_max)

# print(min(result))

##
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for i in range(n) :
    house.append(int(input()))

house.sort()

start = 1 # min gap
end = house[-1] - house[0] # max gap
result = 0

while start <= end :
    mid = (start+end) // 2
    x = house[0]
    count = 1

    for i in range(1,n):
        if house[i] >= x + mid :
            x = house[i]
            count += 1
    if count >= c:
        start = mid + 1
        result = mid
    else :
        end = mid - 1

print(result)
