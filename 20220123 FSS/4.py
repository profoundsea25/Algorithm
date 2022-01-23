def is_exist(i, seq_list) :
    for n in range(len(seq_list)-1, -1, -1) :
        if seq_list[n][0] <= i :
            return n
    else :
        return -1

def solution(truck, w):   
    answer = []
    seq_list = [[0,0]] # (무게, 위치)

    for i in w :
        n = is_exist(i, seq_list)
        if n != -1 :
            for j in range(seq_list[n][1], len(truck)) :
                if i <= truck[j] :
                    answer.append(j+1)
                    seq_list.append([i,j])
                    truck[j] -= i
                    break
            else :
                answer.append(-1)
        if n == -1 :
            for j in range(len(truck)) :
                if i <= truck[j] :
                    answer.append(j+1)
                    seq_list.append([i,j])
                    truck[j] -= i
                    break
            else :
                answer.append(-1)
        seq_list.sort(key = lambda x : x[0])

    return answer


truck = [1,4,5,2,4]
w = [2,4,4,3,2]

# truck = [2,7,4,9]
# w = [7,6,8]
print(solution(truck,w))