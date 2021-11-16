from itertools import combinations

n = int(input())
gap = 1e9
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

combs = list(combinations(list(range(len(data))), n//2))

# for comb in combs:
#     a = 0
#     comb2 = []
#     for i in range(n):
#         if i not in comb:
#             comb2.append(i)
#     for i in comb :
#         for j in comb :
#             a += data[i][j]
#     for i in comb2 :
#         for j in comb2 :
#             a -= data[i][j]
#     a = abs(a)
#     gap = min(gap, a)

for i in range(len(combs)//2):
    a = 0
    for j in combs[i]:
        for k in combs[i]:
            a += data[j][k]
    for j in combs[-1-i]:
        for k in combs[-1-i]:
            a -= data[j][k]
    gap = min(gap, abs(a))

print(gap)