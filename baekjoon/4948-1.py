n = int(input())

def prime_list(n):
    plist = [False] * (n+1)
    plist[1] = True
    for i in range(2, int(n**(1/2))+1):
        if plist[i] == False :
            for j in range(i+i, n+1, i):
                plist[j] = True       
    return plist

while n != 0 :
    plist = prime_list(2*n)
    plist = plist[n+1:]
    print(plist.count(False))
    n = int(input())


# 코드 개선
def prime_list(n):
    plist = [False] * (n+1)
    plist[1] = True
    for i in range(2, int(n**(1/2))+1):
        if plist[i] == False :
            for j in range(i+i, n+1, i):
                plist[j] = True       
    return [p for p in range(2,n+1) if plist[p] == False]

while True :
    n = int(input())
    if n == 0 :
        break

    plist = prime_list(2*n)
    answer = [i for i in plist if i > n]
    print(len(answer))