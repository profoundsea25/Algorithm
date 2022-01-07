# Q 29 공유기 설치, p.369 / 559
n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))

house.sort()
c -= 2

start = 0
end = n-1

lan = [house[start],house[end]]

def bisect(start,end,house,c):
    if start > end :
        return None
    if c == 0:
        return None
    mid = (start+end)//2
    lan.append(house[mid])
    if house[mid]-house[start] > house[end]-house[mid]:
        return bisect(start, mid-1, house, c-1)
    else :
        return bisect(mid+1, end, house, c-1)