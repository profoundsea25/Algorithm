# Q 06 무지의 먹방 라이브, p.317 / 513
food_times = list(map(int, input().split()))
k = int(input())

def solution (food_times, k) :
    if sum(food_times) <= k:
        return -1
    else :
        c = 0
        for _ in range(k) :
            if food_times[c] > 0 :
                food_times[c] -= 1
                c += 1
                if c == len(food_times) :
                    c %= len(food_times)
            elif (food_times[c] == 0) :
                while food_times[c] == 0 :
                    c += 1
                    if c == len(food_times) :
                        c %= len(food_times)
                food_times[c] -= 1
                c += 1
                if c == len(food_times):
                    c %= len(food_times)
        return (c + 1)

result = solution(food_times, k)
print(result)