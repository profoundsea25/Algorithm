# <3> 개미전사 p.220~222
n = int(input())

array = list(map(int, input().split()))

d = [0] * 100

# 수열 왼쪽부터 창고를 털었을 때 얻을 수 있는 최대값을 구함.
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])