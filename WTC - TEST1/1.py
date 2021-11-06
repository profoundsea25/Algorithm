def solution(arr):
    ott = [0,0,0]
    for i in arr :
        if i == 1 :
            ott[0] += 1
        elif i == 2 :
            ott[1] += 1
        elif i == 3 :
            ott[2] += 1
    cri = max(ott)
    answer = [0,0,0]
    for i in range(3) :
        answer[i] = cri - ott[i]
    return answer


arr = [1,2,2,1,3,3]
print(solution(arr))