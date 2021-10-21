import sys
input = sys.stdin.readlines

sentences = []
sentences = input()

def is_correct(sentence):
    stack = []
    for char in sentence :
        if char == '(':
            stack.append(1)
        elif char == ')':
            if not stack :
                return "no"
            elif stack[-1] == 2 :
                return "no"
            elif stack[-1] == 1:
                stack.pop()
        elif char == '[':
            stack.append(2)
        elif char == ']':
            if not stack:
                return "no"
            elif stack[-1] == 1 :
                return "no"
            elif stack[-1] == 2:
                stack.pop()
        elif char == '.':
            break
    if stack :
        return "no"
    else :
        return "yes"

for sentence in sentences :
    if sentence[0] != '.':
        print(is_correct(sentence))
    else :
        pass