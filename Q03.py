# Q03 문자열 뒤집기, p.313 / p.508

n = input()

to1 = 0
to0 = 0

if len(n) > 1:
    for i in range(len(n)-1) :
        if int(n[-1]) == 0 :
            to1 += 1
        if int(n[i]) == 0 and int(n[i+1]) == 1:
            to1 += 1
        else : 
            continue

    for i in range(len(n)-1) :
        if int(n[-1]) == 1:
            to0 += 1
        if int(n[i]) == 1 and int(n[i+1]) == 0 :
            to0 += 1
        else :
            continue

    if to1 < to0 :
        print(to1)
    else :
        print(to0)
else :
    print(0)


## 좀 더 간결하게

n = input()

to1 = 0
to0 = 0

if len(n) > 1:
    for i in range(len(n)-1) :
        if int(n[-1]) == 0 :
            to1 += 1
        else :
            to0 += 1
        
        if int(n[i]) == 0 and int(n[i+1]) == 1:
            to1 += 1        
        elif int(n[i]) == 1 and int(n[i+1]) == 0 :
            to0 += 1
        else : 
            continue
        
    print(min(to1, to0))
else :
    print(0)