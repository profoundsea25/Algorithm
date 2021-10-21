n = int(input())
sort_list = []
for i in range(n):
    x, y = map(int, input().split())
    sort_list.append((x,y))

sort_list.sort(key=lambda x: x[0])
sort_list.sort(key=lambda x: x[1])

for i in sort_list:
    print(i[0], i[1])
