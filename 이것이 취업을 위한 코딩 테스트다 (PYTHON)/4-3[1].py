data = input()
row = int(data[1]) # input()은 스트링으로 받기 때문에, 숫자계산을 위해서는 int로 바꿔야 한다.
column = int(ord(data[0])) - int(ord('a')) + 1 # int(ord('문자')) = 문자를 숫자로
count = 0

steps = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]

for step in steps :
    next_row = row + step[0]
    next_column = column + step[1]
    if next_column >= 1 and next_column <= 8 and next_row >= 1 and next_row <= 8 :
        count += 1

print(count)
