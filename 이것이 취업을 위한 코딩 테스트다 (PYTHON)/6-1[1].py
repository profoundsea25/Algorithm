# p.159 선택 정렬 소스코드
array = []

for i in range(len(array)):
    min_i = i
    for j in range(i+1,len(array)):
        if array[min_i] > array[j]:
            min_i = j
    array[i], array[min_i] = array[min_i], array[i]

print(array)
