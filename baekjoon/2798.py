from itertools import combinations

n, m = map(int, input().split())

numbers = list(map(int,input().split()))

combs = list(combinations(numbers, 3))
max = 0

for i in combs :
    if sum(i) <= m and sum(i) > max :
        max = sum(i)

print(max)