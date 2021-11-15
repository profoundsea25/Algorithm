n = int(input())
op = list(input().split())
mx = ""
mn = ""
c = [False] * 10

def possible(i,j,k):
    if k == '>' :
        return i > j
    elif k == '<':
        return i < j

def solution(count, string):
    global mx, mn
    if count == n+1 :
        if not len(mn):
            mn = string
        else :
            mx = string
        return
    
    for i in range(10):
        if not c[i] :
            if count == 0 or possible(string[-1], str(i), op[count-1]):
                c[i] = True
                solution(count+1, string+str(i))
                c[i] = False

solution(0,"")
print(mx)
print(mn)