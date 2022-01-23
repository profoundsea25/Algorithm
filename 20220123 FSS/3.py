import math

# 코사인 값을 구하기 위한 함수
# (x,y) ~ (0,0) ~ (target_x, target_y) 사이의 cos값을 구하는 과정 
def calc_cos(x, y, target_loc) :
    a = math.sqrt(x**2+y**2)
    b = math.sqrt(target_loc[0]**2+target_loc[1]**2)
    c = math.sqrt((x-target_loc[0])**2 + (y-target_loc[1])**2)
    target_cos = (a**2 + b**2 - c**2) / (2*a*b)
    return b, target_cos
    # b는 (0,0)에서 target까지의 거리이기도 함.

def solution(x, y, r, d, target):
    answer = 0
    for target_loc in target :
        target_r, target_cos = calc_cos(x, y, target_loc)
        # 파이썬의 cos함수는 라디안을 받아야 하므로, d * math.pi / 180을 사용하고,
        # 오차를 처리해주기 위해 소숫점 7번째자리 수에서 반올림
        if target_r <= r and math.cos((d * math.pi) / 180) <= round(target_cos, 7) :
            answer += 1
    return answer

target = [[0, 1], [-1, 1], [1, 0], [-2, 2]]
print(solution(-1,2,2,60,target))