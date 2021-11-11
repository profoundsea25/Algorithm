from itertools import combinations

while True :
    data = list(map(int, input().split()))

    if data == [0] :
        break

    answer = list(combinations(data[1:],6))

    for i in answer :
        print(' '.join(map(str, i)))
    print()