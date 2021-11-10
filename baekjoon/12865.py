import sys
input = sys.stdin.readline

n, k = map(int, input().split())

data = [[0,0]] # 0번 째 물건 삽입해줌 (i-1 계산을 쉽게 하기 위해)
dp = [[0]*(k+1) for _ in range(n+1)] # 0번 째 행/열을 주기 위해 +1 씩 함
# dp는 가로축이 0~k까지의 가방의 남은 무게, 세로축은 data[i]의 정보.

for i in range(n):
    data.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= data[i][0]: # j만큼의 무게가 아이템의 무게보다 크면
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-data[i][0]] + data[i][1])
        else :
            dp[i][j] = dp[i-1][j]

print(n,k)