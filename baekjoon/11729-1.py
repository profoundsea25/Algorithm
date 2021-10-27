n = int(input())

def hanoi(n,start,end):
    if n == 1:
        return print(start, end)
    
    # 1단계 n-1개의 원판을 2번째 막대로 모두 옮긴다.
    hanoi(n-1,start,6-start-end)
    # 2단계 가장 큰 원판을 3번째 막대로 옮긴다.
    print(start,end)
    # 3단계 n-1개의 2번째 막대에 있는 모든 원판을 3번째 막대로 옮긴다.
    hanoi(n-1,6-start-end,end)

print(2**n-1)
hanoi(n,1,3)