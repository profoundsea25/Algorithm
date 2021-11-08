n = int(input())
a = list(map(int, input().split()))

answer = [0 for _ in range(n)]
for i in range(n) :
    for j in range(i):
        # DP Table
        if a[i] > a[j] and answer[i] < answer[j]:
            answer[i] = answer[j]
    answer[i] += 1

print(max(answer))