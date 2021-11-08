n = int(input())
k = int(input())

start = 1
end = k

while start <= end : 
    mid = (start+end) // 2

    count = 0
    for i in range(1,n+1) :
        count += min(mid//i, n)
        if count > k :
            break
    
    if count >= k :
        end = mid - 1
        answer = mid
    else :
        start = mid + 1

print(answer)