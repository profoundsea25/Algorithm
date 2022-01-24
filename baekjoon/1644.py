# https://www.acmicpc.net/problem/1644
# 소수의 연속합
# 2022.01.24 20:27 ~ 21:14

n = int(input())

array = [False]*(n+1)
array[0] = True
array[1] = True
for i in range(2, round(n**(1/2))+1) :
    if array[i] == False :
        for j in range(i*2, n+1, i):
            array[j] = True

prime_list = [p for p in range(n+1) if array[p] == False]

l = len(prime_list)
answer = 0
sum_prime = 0
i = 0
j = 0
while i < l or j < l :
    if sum_prime < n and i == l :
        break
    elif sum_prime < n and i < l:
        sum_prime += prime_list[i]
        i += 1
    elif sum_prime == n :
        answer += 1
        sum_prime -= prime_list[j]
        j += 1
    elif sum_prime > n :
        sum_prime -= prime_list[j]
        j += 1
if sum_prime == n :
    answer += 1

print(answer)