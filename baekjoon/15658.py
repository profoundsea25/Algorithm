n = int(input())
data = list(map(int, input().split()))
op = list(map(int, input().split()))
mx, mn = -1e9, 1e9

def dfs(index, answer, add, sub, mul, div) :
    global mx, mn
    if index == n :
        mx = max(mx, answer)
        mn = min(mn, answer)
        return
    if add :
        dfs(index+1, answer+data[index], add-1, sub, mul, div)
    if sub :
        dfs(index+1, answer-data[index], add, sub-1, mul, div)
    if mul :
        dfs(index+1, answer*data[index], add, sub, mul-1, div)
    if div :
        dfs(index+1, answer//data[index] if answer > 0 else -((-answer)//data[index]), add, sub, mul, div-1)

dfs(1, data[0], op[0], op[1], op[2], op[3])
print(mx)
print(mn)
