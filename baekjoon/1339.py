# https://www.acmicpc.net/problem/1339
# 단어 수학
# 2022.01.16 16:36 ~ 18:00

n = int(input())
# [[10**(자리수)의 합], 수로 나타낸 알파벳]
alpha = [[0, i] for i in range(26)] 
data = []
for i in range(n):
    string = input()
    data.append(string)
    string = string[::-1]
    for j in range(len(string)) :
        index = ord(string[j]) - ord('A')
        alpha[index][0] += 10**(j+1)

alpha.sort(key = lambda x : -x[0])

alpha_map = {}
num = 9
for i in range(len(alpha)) :
    if alpha[i][0] == 0 :
        break
    alpha_map[chr(alpha[i][1] + ord('A'))] = str(num)
    num -= 1

result = 0
for i in range(len(data)) :
    temp = ""
    for j in range(len(data[i])) :
        temp += alpha_map[data[i][j]]
    result += int(temp)

print(result)