a, b, v = map(int, input().split())

def solution(a, b, v):
    day_h = a-b
    real_v = v-a
    result = 0
    day_spent = real_v // day_h
    if real_v % day_h > 0 :
        day_spent = real_v // day_h + 1
    else :
        day_spent = real_v // day_h

    if day_spent == 0 :
        if real_v == 0 :
            result = 1
            return result

    result += day_spent + 1
    return result

print(solution(a,b,v))