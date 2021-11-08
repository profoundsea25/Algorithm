import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for i in range(n):
    house.append(int(input()))

house.sort()

start = 1
end = house[-1] - house[0]

count = 0
while start <= end :
    mid = (start + end) // 2
    installed = house[0]
    count = 1

    for i in range(1, n) :
        if house[i] >= installed + mid :
            installed = house[i]
            count += 1
    
    if count >= c :
        start = mid + 1
        answer = mid
    else :
        end = mid - 1

print(answer)