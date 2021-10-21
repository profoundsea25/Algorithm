m, n = map(int, input().split())

def prime_list(n):
    list = [True] * (n+1)
    list[0] = False
    list[1] = False
    for i in range(2, len(list)):
        if list[i] == True:
            for j in range(i+i, n+1, i):
                list[j] = False
    return list

list_n = prime_list(n)

for i in range(m,n+1):
    if list_n[i] == True:
        print(i)
