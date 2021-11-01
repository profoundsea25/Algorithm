import heapq, sys
input = sys.stdin.readline

n = int(input())

q = []
for i in range(n):
    k = int(input())

    if k == 0 and q == [] :
        print(0)
    elif k == 0 :
        print(-int(heapq.heappop(q)))
    elif k != 0 :
        heapq.heappush(q, -k)