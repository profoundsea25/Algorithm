import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    x = int(input())
    if x :
        stack.append(x)
    else :
        stack.pop()

print(sum(stack))