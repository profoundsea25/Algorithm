# 1차 시도
prime_set = set([])

while True :
    n = int(input())
    if n == 0 :
        break
    
    for i in range(n+1, 2*n+1):
        if i % 2 == 0 :
            if i == 2 :
                prime_set.add(2)
            else :
                continue
        elif i % 3 == 0 :
            if i == 3 :
                prime_set.add(3)
            else :
                continue
        elif i % 5 == 0 :
            if i == 7 :
                prime_set.add(5)
            else :
                continue
        if i % 7 == 0 :
            if i == 7 :
                prime_set.add(7)
            else :
                continue
        else :
            for j in range(1, i//7, 2):
                if j != 1 and i % j == 0 and i != j :
                    break
            else :
                if i == 1 :
                    continue
                else :
                    prime_set.add(i)

print(len(prime_set))

# 2차 시도
while True :
    n = int(input())
    if n == 0 :
        break

    raw_set = set(range(n+1,n*2+1)) - set(range(2,n*2+1,2)) - set(range(3,n*2+1,3)) - set(range(5,n*2+1,5)) - set(range(7,n*2+1,7)) - set([1])
    result_set = set(raw_set)
    
    if n <= 7 :
        for j in range(n+1,2*n+1) :
            if j == 2 :
                result_set.add(2)
            if j == 3 :
                result_set.add(3)
            if j == 5 :
                result_set.add(5)
            if j == 7 :
                result_set.add(7)
    
    for i in raw_set:
        for j in range(1, i//7, 2):
            if j != 1 and i % j == 0 and i != j and i in result_set:
                result_set.remove(i)
        else :
            if i == 1 :
                continue

print(len(result_set))

# 정답
def getPrimaryNum_Eratos(N):
    nums = [True] * (N) 
    for i in range(2, int(N**0.5) + 1): 
        if nums[i] == True: 
            for j in range(i+i ,N, i): 
                nums[j] = False 
    return [i for i in range(2, N) if nums[i] == True] 
                
while True: 
    N = int(input()) 
    if N == 0: 
        break 
    
    prime_list = getPrimaryNum_Eratos(2*N + 1) 
    answer_list = [num for num in prime_list if num > N] 
    print(len(answer_list))
