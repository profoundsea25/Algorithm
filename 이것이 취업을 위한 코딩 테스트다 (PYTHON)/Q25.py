# Q 25 실패율, p.361 / 552
#N = 5 ; stages = [2,1,2,6,2,4,3,3]
#N = 4 ; stages = [4,4,4,4,4]

def solution(N, stages):
    result = []
    stages.sort()
    j = 0
    l = len(stages)
    for i in range(N):
        b = l - j
        c = 0
        while (j < len(stages) and i + 1 == stages[j]):
            c += 1
            j += 1
        a = c
        if b != 0 :
            f = a / b
        else :
            f = 0
        result.append((i+1,f))
    
    result.sort(key=lambda x: -x[1])
    answer = []
    for i in range(len(result)):
        answer.append(result[i][0])
    return answer

#print(solution(N,stages))