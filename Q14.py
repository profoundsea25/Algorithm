# Q 14 외벽 점검, p.335 / 528

def solution(n, weak, dist):
    dist.sort(reverse=True)
    result = 10
    for i in range(len(weak)) :
        drop = []
        count = 0
        k = i
        while(count < len(dist)):
            for x in range(weak[k], weak[k]+dist[count]+1) :
                if x >= n :
                    x -= n
                drop.append(x)
            c = 0
            while(weak[k] in drop):
                k += 1
                c += 1
                if k >= len(weak):
                    k %= len(weak)
                if c > len(weak):
                    break

            j = 0
            for l in range(len(weak)) :
                if weak[l] in drop :
                    j += 1
                else :
                    continue
            if j == len(weak) :
                result = min(result, count+1)
                break
            
            count += 1
            
    if result < 10 :
        return(result)
    else :
        return(-1)
            

#n = 12; weak = [1,5,6,10]; dist = [1,2,3,4]
n = 12; weak = [1,3,4,9,10]; dist = [3,5,7]
print(solution(n,weak,dist))