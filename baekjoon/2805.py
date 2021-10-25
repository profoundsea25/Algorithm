# ??? 어디가 틀린지 모르겠음...
n, m = map(int, input().split())
tree_height = set(map(int,input().split()))

def bi_search(start, end, tree_height, m):
    if start > end :
       return 
    mid = (start + end) // 2
    tree = 0
    for i in tree_height :
        if i > mid :
            tree += i - mid
    if tree < m :
        return bi_search(start, mid-1, tree_height, m)
    elif tree == m :
        return mid
    elif tree > m :
        if bi_search(mid+1,end,tree_height,m) == None :
            return mid
        else :
            return bi_search(mid+1,end,tree_height,m)

result = bi_search(0,max(tree_height),tree_height,m)
print(result)


# 반복문 이진탐색으로 풀기
n, m = map(int, input().split())
a = list(map(int, input().split()))

left, right, ans = 0, max(a), 0
while left <= right:
    mid = (left + right) // 2
    tree = 0
    for i in range(n):
        if mid < a[i]:
            tree += a[i] - mid
    if tree >= m:
        ans = mid
        left = mid + 1
    elif tree < m:
        right = mid - 1

print(ans)