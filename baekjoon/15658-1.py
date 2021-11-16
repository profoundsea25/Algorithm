n = int(input())
data = list(map(int, input().split()))
op = list(map(int, input().split()))

mx, mn = -1e9, 1e9
def dfs(index, value, add, sub, mul, div):
    global mx, mn
    if index != n :
        if add :
            dfs(index+1, value+data[index], add-1, sub, mul, div)
        if sub :
            dfs(index+1, value-data[index], add, sub-1, mul, div)
        if mul :
            dfs(index+1, value*data[index], add, sub, mul-1, div)
        if div :
            dfs(index+1, value//data[index] if value >= 0 else -((-value)//data[index]), add, sub, mul, div-1)
    else :
        mx = max(mx, value)
        mn = min(mn, value)
        return

dfs(1,data[0],op[0],op[1],op[2],op[3])
print(mx)
print(mn)