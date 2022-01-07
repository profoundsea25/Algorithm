# 퀵 정렬 소스코드

array = []

def quick_sort(array, start, end):
    if start >= end : # 예외처리
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right : # 시작
        while left <= end and array[left] <= array[pivot] :
            left += 1 # pivot 왼편은 작은 수들
        while right > start and array[right] >= array[pivot] :
            right -= 1 # pivot 오른편은 큰 수들
        if left > right : # 교차하면 pivot과 right 교체
            array[right], array[pivot] = array[pivot], array[right]
        else : #교차 안하면 left와 right 교체
            array[left], array[right] = array[right], array[left]
        quick_sort(array, start, right-1) # 재귀함수1
        quick_sort(array, right+1, end) # 재귀함수2
    
quick_sort(array, 0, len(array)-1)
print(array)