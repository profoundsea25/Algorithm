n = int(input())
op = input().split()
c = [False]*10
mn = ""
mx = ""

def possible(i,j,k):
    if k == '<' :
        return i < j
    elif k == '>' :
        return i > j

def solve(cnt, s):
    global mx, mn
    if cnt == n + 1 :
        if not len(mn) :
            mn = s
        else :
            mx = s
        return
    for i in range(10):
        if not c[i] :
            if cnt == 0 or possible(s[-1], str(i), op[cnt-1]):
                c[i] = True
                solve(cnt+1, s+str(i))
                c[i] = False

solve(0, "")
print(mx)
print(mn)

## 다시 풀기
n = int(input())
op = input().split()
c = [False] * 10
mx = ""
mn = ""

def possible(i,j,op):
    if op == '<':
        return i < j
    elif op == '>':
        return i > j

def solve(cnt, s):
    global mn, mx
    if cnt == n + 1:
        if not len(mn):
            mn = s
        else :
            mx = s
        return
    for i in range(10):
        if not c[i]:
            if cnt == 0 or possible(s[-1], str(i), op[i-1]):
                c[i] = True
                solve(cnt+1, s+str(i))
                c[i] = False

solve(0,"")
print(mx)
print(mn)


## 다시 풀기 2
n = int(input())
op = input().split()
c = [False] * 10
mx = ""
mn = ""

def possible(i,j,k):
    if k == '>':
        return i > j
    elif k == '<':
        return i < j

def sovle(cnt, s):
    global mx, mn
    if cnt == n+1 :
        if not len(mn):
            mn = s
        else :
            mx = s
        return
    for i in range(10):
        if not c[i]:
            if cnt == 0 or possible(s[-1], str(i), op[i-1]):
                c[i] = True
                possible(cnt+1,s+str(i))
                c[i] = False

solve(0,"")
print(mx)
print(mn)