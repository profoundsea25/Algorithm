n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    a, b = max(x, y), min(x, y)
    t = 1
    while t > 0 :
        t = a % b
        a, b = b, t

    print(int(x*y/a)) 