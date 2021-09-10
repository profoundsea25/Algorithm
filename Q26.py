# Q 26 카드 정렬하기, p.363 / 554
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
    sum = data[0]+data[1]
    count = sum
    for i in range(n-2):
        sum += data[i+2]
        count += sum
    sum = count

print(sum)