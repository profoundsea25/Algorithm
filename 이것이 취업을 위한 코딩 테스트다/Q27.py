# Q 27 정렬된 배열에서 특정 수의 개수 구하기 p.367 / p.555

n = 7; x = 2; data = [1,1,2,2,2,2,3]
#n = 7; x = 4; data = [1,1,2,2,2,2,3]


start = 0
end = n-1
def bisect(start, end, x, data):
    if x not in data :
        return -1
    mid = (start+end)//2
    while True :
        if data[start] <= x <= data[mid]:
            mid = (mid+start-1)//2
        elif data[mid] <= x <= data[end]:
            mid = (mid+end-1)//2
        

print(bisect(start, end, x, data))