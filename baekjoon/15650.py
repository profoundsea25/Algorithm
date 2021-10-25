from itertools import combinations

n, m = map(int, input().split())

numbers = list(range(1,n+1))

comb = list(combinations(numbers, m))

for i in comb :
    i = list(i)
    for x in i :
        print(x, end=' ')
    print()