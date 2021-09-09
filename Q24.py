# Q 24 안테나 p.360 / 551
n = int(input())
data = list(map(int, input().split()))

data.sort()
l = len(data)

if l % 2 == 0 :
    print(data[l//2 - 1])
else :
    print(data[l//2])

