# Q 26 카드 정렬하기, p.363 / 554
# 시간 초과
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()

if n == 1 :
    sum = data[0]
elif n == 2:
    sum = data[0]+data[1]
else:
    sum = 0
    count = 0
    while len(data) != 1 :
        sum += data[0]
        data.pop(0)
        sum += data[0]
        data.pop(0)
        count += sum
        data.append(sum)
        data.sort()
        sum = 0
    sum = count

print(sum)