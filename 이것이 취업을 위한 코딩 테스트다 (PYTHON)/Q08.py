# Q 08 문자열 재정렬, p.322 / 516
str = input()
length = len(str)
i = 0
alpha = []
num = 0
checknum = 0

while i < length :
    if str[i] >= "A" and str[i] <= "Z" :
        alpha += str[i]
    else :
        num += int(str[i])
        checknum += 1
    i += 1

alpha.sort()

i = 0
result = ""

while i < len(alpha) :
    result += alpha[i]
    i += 1

if checknum != 0 :
    print(result, num, sep='')
else :
    print(result)