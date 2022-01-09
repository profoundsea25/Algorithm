def solution(rows, columns):
    answer = [[0 for _ in range(columns)] for _ in range(rows)]
    zeros = []
    for i in range(rows):
        for j in range(columns):
            zeros.append([i,j])
            
    r = 0
    c = 0
    answer[r][c] = 1
    zeros.remove([r,c])
    while zeros : 
        check = answer[r][c]
        if answer[r][c] % 2 == 0 :
            r += 1
            r %= rows
        elif answer[r][c] % 2 == 1 :
            c += 1
            c %= columns
        if [r,c] == [0,0] and check % 2 == 0 :
            return answer
        answer[r][c] = check + 1
        if [r,c] in zeros :
            zeros.remove([r,c])
    return answer

rows = 5
columns = 7
print(solution(rows, columns))