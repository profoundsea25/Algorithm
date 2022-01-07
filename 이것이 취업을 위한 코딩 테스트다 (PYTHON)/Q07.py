# Q 07 럭키 스트레이트, p.321 / 515
n = input()
length = len(n)
fore = int(n[0:int(length/2)])
back = int(n[int(length/2):])

countf = 0
countb = 0

while fore >= 1 :
    countf += (fore % 10)
    fore //= 10

while back >= 1 :
    countb += (back % 10)
    back //= 10

if countf == countb :
    print("LUCKY")
else :
    print("READY")