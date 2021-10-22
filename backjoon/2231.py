n = int(input())

for i in range(n):
    div = 0
    for char in str(i) :
        div += int(char)

    cons = i + div
    if cons == n :
        print (i)
        break
else :
    print(0)