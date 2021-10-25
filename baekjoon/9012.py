import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    x = input()
    stack = []
    for j in x :
        if j == '(' :
            stack.append(1)
        elif j == ')' :
            if stack :
                stack.pop()
            else : 
                print('NO')
                break
    else :
        if stack :
            print('NO')
        else : 
            print('YES')