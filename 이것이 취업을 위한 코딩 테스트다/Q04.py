# Q 04 만들 수 없는 금액, p.314 / 509

# 동전 개수 받기
n = int(input())

# 동전 종류 받기
coins = list(map(int, input().split()))
coins.sort()

result = 1

# 만들 수 없는 양의 정수 금액 중 최솟값
for i in range(1, len(coins)) :
    if result < coins[i] :
        break
    result += coins[i]

print(result)

##
for i in coins :
    if result < i :
        break
    result += i

print (result)