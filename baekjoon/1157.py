target = input()

target = target.upper()
array = [0] * 26
count_set = set()

for i in target :
    if i in count_set:
        array[ord(i)-ord('A')] += 1
    else :
        count_set.add(i)
        if array[ord(i)-ord('A')] == 0:
            array[ord(i)-ord('A')] += 1

most_occured_number = max(array)
if array.count(most_occured_number) == 1 :
    print(chr(ord('A') + array.index(most_occured_number)))
else :
    print("?")  