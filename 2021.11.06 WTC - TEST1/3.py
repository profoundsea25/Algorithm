def solution(ings, menu, sell):
    ings_d = {}
    for i in ings :
        ing_name, ing_price = i.split()
        ings_d[ing_name] = int(ing_price)
        
    menu_d = {}
    for i in menu :
        menu_name, ing_list, menu_price = i.split()
        menu_d[menu_name] = [ing_list, int(menu_price)]

    answer = 0
    for i in sell :
        menu_name, sell_count = i.split()
        raw = 0
        for j in menu_d[menu_name][0] :
            raw += ings_d[j]
        margin = menu_d[menu_name][1] - raw
        answer += margin * int(sell_count)

    return answer

ings = ["r 10", "a 23", "t 124", "k 9"]
ings = ["x 25", "y 20", "z 1000"]
menu = ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"]
menu = ["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"]
sell = ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]
sell = ["BBBB 3", "TTT 2"]
print(solution(ings, menu, sell))
# 1161, -80