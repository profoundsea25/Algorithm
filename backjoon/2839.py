n = int(input())

def solution(n) :
    if n % 5 == 0 :
        return n // 5
    
    k = n // 5
    while k >= 0 :
        if (n - k*5) % 3 == 0 :
            return k + (n - k*5) // 3
        else :
            k -= 1
    return -1

print(solution(n))