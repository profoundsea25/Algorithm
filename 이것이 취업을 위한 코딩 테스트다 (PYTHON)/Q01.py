# Q 01 모험가 길드, p.311 / p.506

# 마을의 모험가 수(N) 입력 받기
n = int(input())

# 공포도 입력 받기
fear = list(map(int, input().split()))

# 공포도 정렬
fear.sort()

# 그룹 나누기
count = 0
i = 0
x = 0

while (i < n) :
    x = fear[i]
    if (i+x-1 <= n) and (fear[i+x-1] == fear[i]) :
        count += 1
        i += x
    else : 
        i += 1

print(count)