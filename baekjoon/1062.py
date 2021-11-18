## 시간초과
# from itertools import combinations
# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())

# words = set()
# alphabets = set()
# antatica = set(list('antatica'))

# for i in range(n):
#     w = input()
#     a = list(w[4:-5])
#     for alpha in a :
#         if alpha not in antatica :
#             alphabets.add(alpha)
#     words.add(w)

# def possible(k) :
#     if k < 5 :
#         return 0
#     elif k == 5 :
#         count = 0
#         for word in words :
#             for alpha in set(word[:0]) :
#                 if alpha not in antatica :
#                     break
#             else :
#                 count += 1
#         return count
#     else :
#         k = k - 5
#         answer = 0
#         for comb in set(combinations(alphabets,k)) :
#             count = 0
#             for word in words :
#                 if len(word) == 8 :
#                     count += 1
#                     continue
#                 for alpha in set(word[4:-5]) :
#                     if alpha not in comb and alpha not in antatica :
#                         break
#                 else :
#                     count += 1
#             answer = max(answer, count)
#         return answer

# print(possible(k))


## 시간 초과 
# from itertools import combinations
# import sys
# input = sys.stdin.readline

# words = []
# n, k = map(int, input().split())
# alphabets = set()
# antatica = set('antatica')

# for i in range(n):
#     word = input().rstrip()
#     for alphabet in word[4:-4] :
#         alphabets.add(alphabet)
#     words.append(word)

# alphabets = alphabets - antatica

# def solution(k):
#     if k < 5 :
#         return 0
#     elif k == 5 :
#         return five()
#     else :
#         return over_five()

# def five() :
#     count = 0
#     for word in words :
#         if set(word) in antatica :
#             count += 1
#     return count

# def over_five() :
#     answer = 0
#     for combs in set(combinations(alphabets,k-5)):
#         count = 0
#         for word in words :
#             word = set(word) - antatica
#             if word & set(combs) == word or not set(word):
#                 count += 1
#         answer = max(answer, count)
#     return answer

# print(solution(k))


## 구글링
import sys

n, k = map(int, input().split())

if k < 5:
    print(0)
    exit()

if k == 26:
    print(n)
    exit()

answer = 0
words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
learn = [0] * 26

for c in set(list('antatica')) :
    learn[ord(c) - ord('a')] = 1

def dfs(idx, cnt) :
    global answer

    if cnt == k - 5 :
        readcnt = 0
        for word in words:
            check = True
            for w in word :
                if not learn[ord(w)-ord('a')]:
                    check = False
                    break
            if check :
                readcnt += 1
        answer = max(answer, readcnt)
        return
        
    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt+1)
            learn[i] = False

dfs(0,0)
print(answer)