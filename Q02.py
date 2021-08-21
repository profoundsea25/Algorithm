# Q 02 곱하기 혹은 더하기, p.312 / p.507~508
n = input()

result = 0

for i in n :
    if result <= 1 :
        result += int(i)
    elif i == 0 or i == 1:      ## i <= 0 으로 간결히 쓸 수 있음
        result += int(i)
    else :
        result *= int(i)

print(result)