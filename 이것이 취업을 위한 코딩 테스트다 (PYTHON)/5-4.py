def recursive_funtion(i) :
    # 100번째 출력했을 떄 종료되도록 종료 조건 명시
    if i == 100 :
        return
    print(i, "번째 재귀 함수에서", i+1, '번째 재귀 함수를 호출합니다.')
    recursive_funtion(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')

recursive_funtion(1)