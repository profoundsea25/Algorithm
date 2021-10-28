import sys
input = sys.stdin.readline

n = int(input())

array = [0] * 101

def solution(k):
    if k <= 3 :
        array[k] = 1
        return array[k]
    
    if array[k] :
        return array[k]
    
    array[k] = solution(k-3)+solution(k-2)
    return array[k]

for i in range(n):
    k = int(input())
    
    print(solution(k))