n = int(input())
array = list(map(int, input().split()))

result = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if array[i] > array[j] and result[i] < result[j] :
            result[i] = result[j]
    result[i] += 1
print(max(result))

## 안 보고 로직 생각하면서 작성
n = int(input())
array = list(map(int, input().split()))

# 다이나믹 프로그래밍을 위한 테이블 생성
result = [0 for _ in range(n)]


for i in range(n):
    # array를 하나 씩 보면서
    for j in range(i):
        # array 처음부터 array[i] 전 까지 다시 반복문을 돌리면서,
        # array[i]와 array[j]를 비교. 만약 array[i]가 array[j]보다 크면서,
        # DP테이블에서 result[i]가 result[j]보다 작으면, result[i] = result[j]로 설정.
        # 즉, result[i]와 result[j]가 증가하는 수열에 있으므로, result[j]의 숫자를 계승받음. 가장 마지막의 += 1로 가장 긴 증가하는 수열의 길이를 저장할 수 있음. 
        if array[i] > array[j] and result[i] < result[j]:
            result[i] = result[j]
    # 가장 긴 수열의 길이를 위해 1은 최소한 증가하도록 설정
    result[i] += 1

print(max(result))