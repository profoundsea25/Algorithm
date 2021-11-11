from itertools import combinations

n = int(input())
data = list(map(int, input().split()))
result = []

for i in range(1,n+1):
    answer = list(combinations(data,i))
    for j in answer :
        check = sum(j)
        result.append(check)

result.sort()

i = 1
for j in result :
    if (i == j) :
        i += 1
    elif i > j :
        pass
    else :
        print(i)
        break
else :
    print(i)