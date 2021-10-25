n = int(input())

k = n
count = 0

j = 0
for i in str(k):
    j += int(i)

l = j % 10

k = int(i)*10 + l
count += 1

while(k != n):
    j = 0
    for i in str(k):
        j += int(i)

    l = j % 10

    k = int(i)*10 + l
    count += 1

print(count)