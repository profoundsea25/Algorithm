# 피보나치 수열 (재귀적), p.212
# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현 (탑다운)
def fibo(x):
    if x==1 or x==2 :
        return 1
    if d[x] != 0 :
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]


# 피보나치 수열 (반복적)
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]