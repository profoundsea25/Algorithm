import sys
input = sys.stdin.readline

n = int(input())
series = []
for_most = [0] * 8002

for i in range(n):
    x = int(input())
    for_most[x+4001] += 1
    series.append(x)

avg = round(sum(series)/len(series))
print(avg)

series.sort()
mid = series[len(series)//2]
print(mid)

most = [index for index, value in enumerate(for_most) if value == max(for_most)]
if len(most) > 1 :
    print(most[1]-4001)
else :
    print(most[0]-4001)

ran = max(series)-min(series)
print(ran)


