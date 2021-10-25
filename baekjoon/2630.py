n = int(input())

table = []
w = 0
b = 0

def solution(table):
    global w, b
    n = len(table)
    first = table[0][0]
    for i in range(n):
        for j in range(n):
            if table[i][j] != first :
                temp1=[row[0:n//2] for row in table[0:n//2]]
                temp2=[row[n//2:n] for row in table[0:n//2]]
                temp3=[row[0:n//2] for row in table[n//2:n]]
                temp4=[row[n//2:n] for row in table[n//2:n]]
                return solution(temp1), solution(temp2), solution(temp3), solution(temp4)

    if first == 0 :
        w += 1
    else :
        b += 1

for i in range(n):
    table.append(list(map(int,input().split())))

solution(table)
print(w)
print(b)