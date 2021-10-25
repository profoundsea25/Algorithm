n, m = map(int, input().split())
series = list(map(int, input().split()))

queue = list(range(1,n+1))
count = 0

for i in series :
    idx = queue.index(i)
    
    if idx == 0 :
        pass
    elif idx <= len(queue) // 2 :
        for _ in range(idx):
            a = queue.pop(0)
            queue.append(a)
            count += 1
    elif idx > len(queue) // 2 :
        for _ in range(len(queue) - idx):
            a = queue.pop()
            queue.insert(0,a)
            count += 1

    queue.pop(0)

print(count)