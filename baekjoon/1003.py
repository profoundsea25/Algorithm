n = int(input())

for i in range(n):
    k = int(input())
    zero = [1, 0]
    one = [0, 1]
    for i in range(k-1):
        zero.append(zero[-1]+zero[-2])
        one.append(one[-1]+one[-2])
    if k == 0 :
        print(zero[0],one[0])
    else :
        print(zero[-1], one[-1])