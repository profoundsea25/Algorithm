# Q 05 볼링공 고르기, p.315 / 512

n, m = map(int, input().split())
ball = list(map(int, input().split()))

count = 0

for i in range(0, n-1) : 
    for j in range(i+1, n) :
        if ball[i] != ball[j] :
            count += 1

print (count)