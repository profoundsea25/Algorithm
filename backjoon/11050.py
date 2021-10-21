n, m = map(int,input().split())

def facto(n):
    if n == 1 or n == 0:
        return 1
    return n*facto(n-1)

result = facto(n) / facto(m) / facto(n-m)

print(int(result))