target = input()
count = 0
i = 0
while i < len(target) :
    if i+1 < len(target) :
        if target[i] == 'c':
            if target[i+1] in ['=','-']:
                i += 1
        elif target[i] == 'd':
            if target[i+1] == '-':
                i += 1
            elif i+2< len(target) and target[i+1] == 'z' and target[i+2] == '=':
                i += 2
        elif target[i] in ['l','n']:
            if target[i+1] == 'j':
                i += 1
        elif target[i] in ['s','z']:
            if target[i+1] == '=':
                i += 1
    count += 1
    i += 1

print(count)


# 개 쉽게 푸는 방법
s = ['c=','c-','dz=','d-','lj','nj','s=','z=']
string = input()
cnt=0
for x in s:
   string = string.replace(x, '1')
print(len(string))