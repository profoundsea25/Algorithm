def solution(log):
    total = 0
    for i in range(len(log)//2) :
        start = int(log[2*i][0:2])*60 + int(log[2*i][3:])
        end = int(log[2*i+1][0:2])*60 + int(log[2*i+1][3:])
        study_time = end - start

        if study_time < 5 :
            study_time = 0
        elif study_time > 105 :
            study_time = 105
        total += study_time
        
    hh = str(total // 60)
    mm = str(total % 60)

    if int(hh) < 10 :
        hh = '0' + hh
    if int(mm) < 10 : 
        mm = '0' + mm
    answer = hh+':'+mm
    return answer


log = ["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]
log = ["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]

print(solution(log))
