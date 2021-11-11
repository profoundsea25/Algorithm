n, k = map(int, input().split())

data = [[0,0]]

answer = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    data.append(list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1,k+1):
        if j >= data[i][0] :
            answer[i][j] = max(answer[i-1][j], answer[i-1][j-data[i][0]]+data[i][1])
        else :
            answer[i][j] = answer[i-1][j]

print(answer[n][k])