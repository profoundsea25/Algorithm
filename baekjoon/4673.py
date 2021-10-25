# 출현한 숫자를 기록할 리스트 초기화
array = [0] * 10001

# 셀프넘버 실행함수
def self_number(n) :
    sum_of_number = 0
    m = n * 10
    while (m // 10 != 0) :
        m = m//10
        sum_of_number += m % 10
    return n + sum_of_number

for i in range(1, 10001) :
    if array[i] == 0 :
    # 한번이라도 출현한 숫자가 아니면,
        n = i
        # 셀프넘버가 10000을 넘지 않고,
        while (self_number(n) <= 10000):
            n = self_number(n)
            # 한번이라도 출현한 숫자가 아니면 array의 숫자만큼의 위치 +1
            if array[n] == 0 :
                array[n] += 1
            # 한번이라도 출현 했으면 반복문으로 돌아감
            else :
                break            
    else : 
    # 한번이라도 출현한 숫자라면 건너 뜀
        continue

for i in range(1, 10001):
    if array[i] == 0 :
        print(i)

# 다른 사람의 풀이 (집합과 str 이용)
natural_num = set(range(1,10001))
generated_num = set()

for i in range(1,10001):
    for j in str(i): # 개꿀팁 : str으로 변환하면 자리수 그대로 사용 가능!
        i = i+int(j) # int로 다시 바꿔준다.
    generated_num.add(i)
    
self_num = sorted(natural_num - generated_num)
for m in self_num:
    print(m)