n = int(input())
people = list(map(int, input().split()))
people.sort()

answer = 0

for i in range(len(people)) :
    time = 0
    for j in range(i+1):
        time += people[j]
    answer += time

print(answer)

# 다른 방법

n = int(input())
people = list(map(int, input().split()))
people.sort()

for i in range(1,len(people)):
    people[i] += people[i-1]

print(sum(people))
