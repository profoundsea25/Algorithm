# Q 23 국영수, p.359 / 550

n = int(input())
data = []
for _ in range(n):
    name, kor, eng, math = input().split()
    data.append((name, int(kor), int(eng), int(math)))

data.sort(key=lambda x: (-int(x[1]), int(x[2]), (-int(x[3]), x[0])))

for student in data :
    print(student[0])