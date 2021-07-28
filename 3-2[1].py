n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

chunk_count = m//(k+1)
first_count = chunk_count*k + (m % (k+1))

result = 0
result = (first_count * first) + ((chunk_count) * second)
print(result)