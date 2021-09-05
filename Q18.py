# Q 18 괄호 변환, p.347 / 536

#p = "(()())()"
#p = ")("
p = "()))((()"

def is_balanced(p):
    i = 0
    l = 0
    r = 0
    while(i<len(p)):
        if p[i] == "(":
            l += 1
        else:
            r += 1
        if l == r :
            break
        i += 1
    return i

def is_correct(p):
    i = 0
    l = 0
    r = 0
    while(i<len(p)):
        if p[i] == "(":
            l += 1
        else:
            r += 1
        if l < r :
            return False
        i += 1
    return True

def solution(p):
    if p == "" :
        return p
    i = is_balanced(p)

    u = p[0:i+1]
    if i+1 == len(p):
        v = ""
    else :
        v = p[i+1:]

    if is_correct(u) == True :
        u = u + solution(v)
        return u
    else :
        w = "("
        w = w + solution(v) + ")"
        j = 1
        while(j < len(u)-1) :
            if u[j] == "(" :
                w = w + ")"
            else :
                w = w + "("
            j += 1
        return w
        
print(solution(p))

    