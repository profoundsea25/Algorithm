n, k = map(int, input().split())

data = list(range(1,n+1))
answer = []
index = 0
while data :
    index += k-1
    index %= len(data)
    answer.append(data.pop(index))

result = '<'+str(answer[0])

for i in range(1,len(answer)) :
    result += ', ' + str(answer[i])
result += '>'
print(result)