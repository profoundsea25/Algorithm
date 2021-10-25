n = int(input())
number = 0
stack = []
result = []
is_able = True

for i in range(n):
    x = int(input())

    while number < x :
        number += 1
        stack.append(number)
        result.append("+")
    
    if stack[-1] == x :
        stack.pop()
        result.append("-")
    else:
        is_able = False
        break

if is_able == False :
    print("NO")
else :
    for i in result :
        print(i)


# 
n = int(input())                    # 가장 첫 줄의 수를 받습니다.
number = 0                          # 숫자 역할을 할 변수
stack = []                          # 스택을 위한 리스트
sign = []                           # 부호를 저장하기 위한 리스트
is_able = True                      # 가능한 수열인지 아닌지 참/거짓 저장

for i in range(n):
    x = int(input())                # 숫자를 받는다.(x)

    while number < x :              # 만약 그 숫자(x)가 현재 number보다 작다면
        number += 1                 # 숫자 + 1
        stack.append(number)        # 스택에 넣고
        sign.append("+")            # '+'도 저장

    if x == stack[-1] :             # stack 리스트의 가장 끝과 x가 같다면
        stack.pop()                 # stack.pop
        sign.append("-")            # 부호 리스트에 - 저장
    else :
        is_able = False             # 이 과정이 수행이 안 되면 False(불가능한 수열)
        break

if is_able == False:
    print("NO")
else :
    for i in sign :
        print(i)