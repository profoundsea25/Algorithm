def solution(grade):
    # 학생이 1명이면 무조건 1등이므로 예외 처리
    if len(grade) == 1 :
        return [1]

    sorted_grade = sorted(grade, reverse=True) # 석차를 구하기 위해 성적 데이터를 내림차순으로 정렬
    grade_dict = {}      # 점수와 석차를 매칭할 딕셔너리 정렬 {점수 : 석차} 형식
    grade_count = 1      # 동점자를 나타내는 변수
    number = 1           # 석차를 나타내는 변수

    for i in range(1,len(sorted_grade)) :
        if sorted_grade[i-1] != sorted_grade[i] :       # 내림차순 정렬한 성적데이터의 i-1번째와 i번째가 다를 경우 (즉, 점수가 한 단계 낮아진 경우) 
            grade_dict[sorted_grade[i-1]] = number      # i-1번째 점수의 석차를 딕셔너리에 저장 {점수 : 석차}
            number += grade_count                       # 다음 석차를 위해 동점자 수(grade_count)를 더해주기
            grade_count = 1                             # grade_count 초기화
        else :                                          # i-1번째와 i번째가 같은 경우 (즉, 동점자인 경우)
            grade_count += 1                            # 현재 점수 동점자수 + 1

    # 점수가 가장 낮은(마지막 i번 째) 학생을 위한 예외처리 (위 반복문에서 i, number 변수를 그대로 활용)
    if sorted_grade[i-1] != sorted_grade[i] :           
        grade_dict[sorted_grade[i]] = len(sorted_grade) # 뒤에서 2번째 학생과 점수가 다른 경우, 석차 = 학생수
    else :
        grade_dict[sorted_grade[i]] = number            # 뒤에서 2번째 학생과 점수가 같은 경우, 석차를 나타내는 number 저장 (마지막 석차이기 때문에 동점자 고려 X)

    answer = []
    for i in range(len(grade)) :
        answer.append(grade_dict[grade[i]])             # 성적 데이터를 차례대로 조회해가며 {점수 : 석차} 로 이루어진 grade_dict를 활용해 정답 출력
    return answer