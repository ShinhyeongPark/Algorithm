def solution(table, languages, preference):
    score = []  # 직군별 점수를 저장할 리스트
    answer = []  # 최고 점수인 직군을 저장할 리스트

    # 직군 단위로 통계를 내기 위한 반복
    for t in table:
        tmpScore = 0  # 각 직군별 계산을 위한 변수
        for i, l in enumerate(languages):  # 0,python/1, C++/2, SQL
            if l in t.split()[1:]:  # t의 0번째 값은 직군이므로 계산에 필요없음
                tmpScore += preference[i] * (5 - t.split().index(l) + 1)

        score.append(tmpScore) #저장

    maxScore = max(score)
    for i, s in enumerate(score):
        if s == maxScore:
            answer.append(table[i].split()[0])

    answer.sort()
    return answer[0]
