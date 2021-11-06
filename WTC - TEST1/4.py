def solution(s):
    answer = []
    cri = s[0]
    cnt = 1
    for i in range(1,len(s)) :
        if cri == s[i] :
            cnt += 1
        else :
            answer.append(cnt)
            cnt = 1
            cri = s[i]
    answer.append(cnt)

    if s[0] == s[-1] :
        cnt = answer[0] + answer[-1]
        answer.pop(0)
        answer.pop()
        answer.append(cnt)
    answer.sort()
    return answer

s ="akdkakkaaakaa"
print(solution(s))