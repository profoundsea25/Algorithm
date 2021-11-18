import sys
input = sys.stdin.readline

n, k = map(int, input().split())

if k < 5 :
    print(0)
    exit()
elif k == 26 :
    print(n)
    exit()

answer = 0
# 단어를 스펠링으로 저장 가능
words = [set(input().rstrip()) for _ in range(n)]
learn = [False]*26

for c in set(list('antatica')) :
    learn[ord(c)-ord('a')] = True

def dfs(index, count):
    global answer

    if count == k-5 :
        read_count = 0
        for word in words :
            for char in word :
                if not learn[ord(char)-ord('a')]:
                    break
            else :
                read_count += 1
        answer = max(answer, read_count)
        return 
    
    for i in range(index, 26):
        if not learn[i] :
            learn[i] = True
            dfs(i, count+1)
            learn[i] = False

dfs(0,0)
print(answer)

## 안 보고 짜기
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

if k < 5 :
    print(0)
    exit()
elif k == 26 :
    print(n)
    exit()

words = [set(input().rstrip()) for _ in range(n)]
answer = 0
learn = [False]*26

for c in set('antatica'):
    learn[ord(c)-ord('a')] = True
    
def dfs(index, count) :
    global answer

    if count == k - 5 :
        readable = 0
        for word in words :
            for char in word :
                if not learn[ord(char)-ord('a')]:
                    break
            else :
                readable += 1
        answer = max(answer, readable)
        return

    for i in range(index, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, count+1)
            learn[i] = False

dfs(0,0)
print(answer)