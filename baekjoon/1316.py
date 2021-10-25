n = int(input())
result = 0
for i in range(n):
    sentence = input()
    alpha = set([])
    for k in range(len(sentence)) :
        if k-1 >= 0 and sentence[k-1] != sentence[k] and sentence[k] in alpha:
            break
        else :
            alpha.add(sentence[k])
    else :
        result += 1

print(result)

# 더 좋은 코드
num=eval(input())
ans=0
def func(st):
	cnt=0
	for i in range(1,len(st)):
		if st[i-1]!=st[i]:
			cnt+=1
	if cnt!=len(set(st))-1: # st을 set에 집어 넣고, len 함수 보정을 위해 -1
		return 0 # 연속으로 나타난 것이 아니면서 중복되면 cnt와 우변이 다름
	return 1
for i in range(num):
    st=input()
    ans+=func(st)
print(ans)