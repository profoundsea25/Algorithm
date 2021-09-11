# Q 28 고정점 찾기, p.368 / 558

#n = 5; array=[-15,-6,1,3,7]
#n = 7; array=[-15,-4,2,8,9,13,15]
n = 7; array=[-15,-4,3,8,9,13,15]

def bisect(start, end, array):
    mid = (start+end)//2
    if array[start] == start :
        return start
    elif array[end] == end :
        return end
    elif array[mid] == mid :
        return mid
    elif mid != start+1 and array[mid] < mid :
        return bisect(mid+1, end, array)
    elif mid != end-1 and array[mid] > mid :
        return bisect(start, mid-1, array)
    else :
        return -1

print(bisect(0, n-1, array))


