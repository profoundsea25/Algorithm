n = int(input())
result = []
for i in range(n):
    list = []
    target = 0
    list = input().split()
    avg = sum(int(j) for j in list[1::])/int(list[0])
    for j in list[1::] :
        if int(j) > avg :
            target += 1
    result.append(format(target/int(list[0])*100, '.3f')+"%")

for per in result:
    print(per)