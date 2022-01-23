import math

def solution(b):
    # 이론적인 경우의 수가 최대 500,000이므로 모든 경우의 수를 탐색 
    # a 초기화 (자연수이므로 1로 초기화)
    a = 1
    # a <= b를 만족하는 동안 반복문 수행
    while a <= b :
        # c**2 = a**2 + b**2 
        c_sq = a**2 + b**2
        # 만약 c**2의 루트값의 내림한 수를 다시 제곱을 취했을 때, 이전 값과 같다면 그 때의 c를 return
        c = math.floor(c_sq**(1/2))
        if c**2 == c_sq :
            return c
        # 조건에 만족하지 않은 경우 a를 1씩 늘려 다시 수행
        a += 1
    # a <= b 동안 만족하는 c가 없으면 -1 return
    return -1