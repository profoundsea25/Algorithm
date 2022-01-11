import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
graph = [[] for _ in range(n)]
circle = set()
check = -1
answer = [0] * n

for _ in range(n):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)


def search_circle(now, come_from, track) :
    global circle, check
    
    trace = set(track)
    trace.add(now)

    for next in graph[now] :
        if next == come_from :
            continue
        if next in track :
            circle = set(trace)
            check = next
            return
        search_circle(next, now, trace)


def bfs(node) : 
    q = deque({node})

    while q :
        here = q.popleft()
        for next in graph[here] :
            if next not in circle and answer[next] == 0 :
                answer[next] = answer[here] +1
                q.append(next)
        

search_circle(0, -1, set())
search_circle(check, -1, set())

for i in circle :
    for next in graph[i] :
        if next not in circle:
            answer[next] = 1
            bfs(next)

for i in answer :
    print(i, end = " ")