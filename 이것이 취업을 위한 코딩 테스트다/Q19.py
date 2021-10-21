# Q 19 연산자 끼워 넣기, p.349 / 538
#n = 2; data = [5,6]; oper = [0,0,1,0]
#n = 3; data = [3,4,5]; oper = [1,0,1,0]
#n = 6; data = [1,2,3,4,5,6]; oper = [2,1,1,1]

from itertools import permutations

n = int(input())
data = list(map(int, input().split()))
oper = list(map(int, input().split()))

res_max = 0
check = 0
res_min = 0
result = 0
operation = ["+","-","*","/"]
operlist = []

for i in range(len(oper)):
    for _ in range(oper[i]):
        operlist.append(operation[i])

P_oper = list(permutations(operlist, n-1))

i = 0
while(i < len(P_oper)):
    for j in range(len(P_oper)) :
        result = data[0]
        for k in range(n-1):
            if P_oper[j][k] == "+":
                result += data[k+1]
            elif P_oper[j][k] == "-":
                result -= data[k+1]
            elif P_oper[j][k] == "*":
                result *= data[k+1]
            else :
                if result < 0 :
                    result = -(-(result) // data[k+1])
                else :
                    result //= data[k+1]
        res_max = max(res_max, result)
        if check == 0 :
            res_min = res_max
            check = 1
        res_min = min(res_min, result)
    i += 1
    
print(res_max)
print(res_min)