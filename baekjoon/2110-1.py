import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for i in range(n):
    house.append(int(input()))

# 이진 탐색 필수 조건 : 정렬이 되있어야 한다.
house.sort()

# 집 간 최소 거리
start = 1
# 집 간 최대 거리
end = house[-1] - house[0]

result = 0

# 이진 탐색 시작 (공유기 설치)
while start <= end :
    # 공유기 간 설치 거리 설정
    mid = (start + end) // 2
    # 공유기를 1번 집부터 설치 시작
    location = house[0]
    # 1개를 설치했으므로
    count = 1

    # 2번 집부터 집 간 거리를 재며 공유기 설치 시작
    for i in range(1,n):
        # 만약 i번째 집의 위치가 (그 직전 설치했던 집의 위치) + (설정한 공유기 간 거리)를 초과하면, 
        if house[i] >= location + mid :
            # 그 집에 공유기 설치
            location = house[i]
            # 공유기 설치 개수 + 1
            count += 1

    # 반복문이 마치면 공유기 house[-1]까지 공유기 설치 유무 판단이 끝난 상태
    # 만약 공유기 설치 개수가 조건보다 많으면, 공유기 간 설치 거리를 늘려서 이진 탐색
    if count >= c :
        start = mid + 1
        # 현재 거리가 최대일 수도 있으므로, 여기서 result를 저장
        result = mid
    # 만약 공유기 설치 개수가 조건보다 적으면, 공유기 간 설치 거리를 줄여서 이진 탐색
    else :
        end = mid - 1

# 이진 탐색 결과 출력
print(result)


## 안 보고 로직 구현하기
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for i in range(n):
    house.append(int(input()))

house.sort()

start = 1
end = house[-1] - house[0]
result = 0

while start <= end :
    mid = (start+end) // 2
    location = house[0]
    count = 1

    for i in range(1,n):
        if house[i] >= location + mid :
            location = house[i]
            count += 1
    
    if count >= c :
        start = mid + 1
        result = mid
    else :
        end = mid - 1

print(result)