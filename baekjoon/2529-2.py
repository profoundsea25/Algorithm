n = int(input())
op = list(input().split())
c = [False]*10
mn = ""
mx = ""


def possible(i,j,k):
    if k == '>':
        return i > j
    elif k == "<":
        return i < j

def solution(cnt, s):
    global mn, mx
    if cnt == n +1 :
        if not len(mn):
            mn = s
        else :
            mx = s
        return
        
    for i in range(10):
        if not c[i] :
            if cnt == 0 or possible(s[-1],str(i),op[cnt-1]):
                c[i] = True
                solution(cnt+1, s+str(i))
                c[i] = False

solution(0,"")
print(mx)
print(mn)