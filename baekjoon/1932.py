n = int(input())
tri = []
for i in range(n):
    tri.append(list(map(int,input().split())))

for i in range(1, n):
    for j in range(len(tri[i])):
        if n-1 > 0 and j-1 < 0 :
            tri[i][j] = tri[i-1][j] + tri[i][j]
        elif n-1 > 0 and 0 < j < len(tri[i])-1:
            tri[i][j] = max(tri[i-1][j-1], tri[i-1][j]) + tri[i][j]
        elif n-1 >0 and j == len(tri[i])-1:
            tri[i][j] = tri[i-1][j-1] + tri[i][j]

print(max(tri[-1]))