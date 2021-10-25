n = int(input())

def solution(x1, y1, r1, x2, y2, r2) :
    if x1 == x2 and y1 == y2 and r1 == r2 :
        return -1
    elif x1 == x2 and y1 == y2 and r1 != r2 :
        return 0
    
    dist_bet_tur = ((x1-x2)**2+(y1-y2)**2)**(1/2)
    dist_bet_mar = r1 + r2

    if dist_bet_tur == dist_bet_mar:
        return 1
    elif abs(r1-r2) == dist_bet_tur :
        return 1
    elif dist_bet_tur > dist_bet_mar :
        return 0
    elif dist_bet_tur < dist_bet_mar and abs(r1-r2) < dist_bet_tur :
        return 2
    elif dist_bet_tur < dist_bet_mar and abs(r1-r2) > dist_bet_tur :
        return 0

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    print(solution(x1,y1,r1,x2,y2,r2))
