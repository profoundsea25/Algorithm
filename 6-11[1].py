n = int(input())
array = []
for i in range(n):
    input_data = input().split()
    array.append(input_data[0], int(input_data[2]))

array = sorted(array, key = lambda student: student[1])

for student in range(array): ##
    print(student[0], end = ' ')

# 튜플, lambda 함수 활용 공부하기
