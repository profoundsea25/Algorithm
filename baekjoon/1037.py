n = int(input())
array = list(map(int, input().split()))

array.sort()

result = array[0] * array[-1]
print(result)