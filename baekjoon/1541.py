expression = input()
number = expression[0]
series = []

for i in range(1,len(expression)):
    if expression[i] != '+' and expression[i] != '-':
        if i-1 != 0 and expression[i-1] == '-':
            number += '-'
        number += expression[i]
    else:
        series.append(number)
        number = ''
series.append(number)

answer = int(series[0])

for i in range(1,len(series)):
    if '-' in series[i-1] and '-' not in series[i]:
        series[i] = '-' + series[i]
    answer += int(series[i])

print(answer)
