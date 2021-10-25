n = int(input())
result = []

def solution (x,y):
    if y-x == 1:
        return 1
    elif y-x == 2:
        return 2
    elif y-x == 3:
        return 3
    elif y-x == 4:
        return 3

    dist_left = y-x
    k = 0
    count = 0
    sum_dist = 0
    while True :
        dist_left = y-x
        k += 1
        sum_dist += k
        count += 2
        dist_left -= 2*sum_dist
        if dist_left <= 2*(k+1) :
            break

    if dist_left == 0 :
        return count
    elif dist_left <= k+1 :
        return count + 1
    else :
        return count + 2
            
for i in range(n):
    x, y = map(int, input().split())
    result.append(solution(x,y))

for i in result :
    print(i)
