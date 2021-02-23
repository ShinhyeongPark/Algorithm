T = int(input()) #총 테스트 케이스 수

for t in range(T):
    record = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

    info = list(map(int, input().split())) #학생 수, 찾고자하는 학생 번호 !1부터 시작
    score_stack = [] #총점 저장소
    record_stack = [] #N/10만큼 동일한 학점을 저장할 스택
    cycle = int(info[0]/10) #N/10

    for i in range(info[0]): #학생수 만큼 반복
        scores = list(map(int, input().split())) #H,M,H,M
        score_stack.append(scores[0] * 0.35 + scores[1] * 0.45 + scores[2] * 0.2) #주어진 조건에 따른 총점 계산
    find = score_stack[info[1]-1] #찾고자하는 총점
    score_stack.sort(reverse=True) #내림차순 정렬

    #사이클만큼 동일한 학점을 부여
    count = 0
    while len(record_stack) != len(score_stack):
        for j in range(cycle):
            record_stack.append(record[count])
        count += 1
    
    #찾고자하는 총점의 score_stack에서의 위치 = record_stack에서의 위치
    print("#"+str(t+1), record_stack[score_stack.index(find)])
