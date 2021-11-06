def solution(time, plans):
    traveled = []
    for plan in plans :
        
        if plan[1][-2:] == "AM" and int(plan[1][:-2]) > 9 :
            time -= 18 - int(plan[1][:-2])
        elif plan[1][-2:] == "AM" and int(plan[1][:-2]) <= 9 :
            time -= 8.5
        elif plan[1][-2:] == "PM" and int(plan[1][:-2]) < 6 :
            time -= 6 - int(plan[1][:-2])
        
        if plan[2][-2:] == "PM" and int(plan[2][:-2]) > 1 and int(plan[2][:-2]) <= 6:
            time -= int(plan[2][:-2]) - 1
        elif plan[2][-2:] == "PM" and int(plan[2][:-2]) > 6 :
            time -= 5

        if time >= 0 :
            traveled.append(plan[0])
        elif time < 0 :
            return traveled[-1]
    return traveled[-1]



time = 3.5
plans = [["홍콩", "11PM", "9AM"], ["엘에이", "1AM", "2PM"]]
print(solution(time, plans))