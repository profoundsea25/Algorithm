n = int(input())

def fact(n):
    if n==0 or n==1 :
        return 1
    else :
        return n*fact(n-1)

for i in range(n):
    m, k = map(int, input().split())
    
    result = fact(k) / (fact(m) * fact(k-m))
    # 곱셈, 나눗셈에도 순서 중요!!! 
    print(int(result))