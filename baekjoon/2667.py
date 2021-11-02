n = int(input())

data = []

for i in range(n):
    data.append(list(input()))

def dfs(number, i, j) :
    global data
    data[i][j] = number
    if i > 0 and data[i-1][j] == 1:
        dfs(number, i-1,j)
    if i+1 < n and data[i+1][j] == 1:
        dfs(number, i+1, j)
    if j > 0 and data[i][j-1] == 1:
        dfs(number, i, j-1)
    if j+1 < n and data[i][j+1] == 1:
        dfs(number, i, j+1)
    return 1

number = 2

for i in range(n):
    for j in range(n):
        data[i][j] = int(data[i][j])

for i in range(n):
    for j in range(n):
        if data[i][j] == 1 :
            if dfs(number, i, j) == 1:
                number += 1

answer_number = number - 2

answer_list = [0] * number
for i in range(n):
    for j in range(n):
        answer_list[data[i][j]] += 1

answer_list = answer_list[2:]
answer_list.sort()

print(answer_number)
for i in answer_list:
    if i != 0 :
        print(i)