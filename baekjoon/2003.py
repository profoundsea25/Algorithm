n, m = map(int, input().split())
data = list(map(int, input().split()))

count = 0

for i in range(n):
    s = 0 
    for j in range(i,n):
        s += data[j]
        if s == m :
            count += 1
            break
        elif s > m :
            break

print(count)