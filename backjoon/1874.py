import sys
input = sys.stdin.readline

n = int(input())
target = []

for i in range(n):
    target.append(int(input()))

def is_correct(target):
    sign = []
    for i in range(target[0]):
        sign.append('+')
    sign.append('-')

    if sign.count('+') < max(target):
        for i in range(target.index(max(target))+1):
            if target[i-1] - target[i] == 1 :
                sign.append('-')
            elif target[i-1] - target[i] > 1 :
                return print('NO')
            elif target[i-1] < target[i] :
                cnt = sign.count('-')
                for _ in range(cnt):
                    sign.append('+')

    if sign.count('+') < max(target) :
        for i in range(len(target)-target.index(max(target))+1):
            if target[i-1] < target[i] :
                return print('NO')
            else :
                sign.append('-')
    
    for i in sign :
        print(i)

is_correct(target)

# 정답
n = int(input())
count = 0
stack = []
result = []
no_message=True

for i in range(0,n):
    x = int(input())

    while count < x:
      count += 1
      stack.append(count)
      result.append("+")

    if stack[-1]==x:
        stack.pop()
        result.append("-")
    else:
        no_message = False
        break

if no_message==False:
    print("NO")
else:
    for i in result:
        print(i)