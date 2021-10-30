import sys
input = sys.stdin.readline

n, k = map(int, input().split())

money = []
for i in range(n):
    money.append(int(input()))

count = 0
for i in range(n-1,-1,-1):
    if money[i] > k :
        pass
    elif k != 0:
        count += k // money[i]
        k %= money[i]
    elif k == 0 :
        break

print(count)