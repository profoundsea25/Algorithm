# Q 13 치킨 배달, p.332 / 527
# combinations (조합) 함수 처음으로 다뤄봄
from itertools import combinations

n, m = map(int, input().split())
city = []
for _ in range(n) :
    city.append(list(map(int, input().split())))

chicken = []
home = []

for i in range(n) :
    for j in range(n) :
        if city[i][j] == 2 :
            chicken.append((i,j))
        elif city[i][j] == 1 :
            home.append((i,j))

comb = list(combinations(chicken, m))

def chicken_distance(comb, home) :
    result = []
    for x in comb :
        sum_distance = 0
        for h in home :
            distance = 100
            for i in x :
                distance = min(distance, abs(i[0]-h[0]) + abs(i[1]-h[1]))
            sum_distance += distance
        result.append(sum_distance)
    
    result.sort()
    return result[0]

result = chicken_distance(comb, home)
print(result)