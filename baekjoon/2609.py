a, b = map(int, input().split())

c, d = max(a, b), min(a, b)
t = 1
while t > 0 :
    t = c % d
    c, d = d, t

print(c)
print(int(a*b/c))