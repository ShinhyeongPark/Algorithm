#올바른 결과값을 리턴하나
#효율성에서 문제가 있다.
#반복문의 잦은 사용과 중첩적으로 반복문을 사용해서 효율성이 떨어진다.

def solution(infos, querys):
    info_split = [] #지원자 정보 분리한 결과
    query_split = [] #문의조건 분리한 결과
    stack = [0] * len(querys) #조건에 만족하는 지원자 수(최종 Return)
    
    for info in infos: #지원자 정보는 단순하게 공백으로 분리한다.
        info_split.append(info.split(' '))
    #지원자 정보 분리 결과
    #[['java', 'backend', 'junior', 'pizza', '150'], 
    # ['python', 'frontend', 'senior', 'chicken', '210'], 
    # ['python', 'frontend', 'senior', 'chicken', '150'], 
    # ['cpp', 'backend', 'senior', 'pizza', '260'], 
    # ['java', 'backend', 'junior', 'chicken', '80'], 
    # ['python', 'backend', 'senior', 'chicken', '50']]
    
    for query in querys: #쿼리문은 공백과 and가 함께 있기 때문에
        text = query.split(" ") #먼저 공백으로 제거한 후
        while "and" in text: #리스트에 and가 있을 경우, and가 존재하지 않을 때까지 제거
            text.remove("and")
        query_split.append(text)
    #문의조건 분리 결과
    #[['java', 'backend', 'junior', 'pizza', '100'],
    # ['python', 'frontend', 'senior', 'chicken', '200'],
    # ['cpp', '-', 'senior', 'pizza', '250'], 
    # ['-', 'backend', 'senior', '-', '150'], 
    # ['-', '-', '-', 'chicken', '100'], 
    # ['-', '-', '-', '-', '150']]
    
    #'-'은 어떤 항목이든 고려하지 않기때문에
    #인덱스 위치에 따라 해당하는 조건을 추가했다.
    for qs in query_split: #쿼리 한문장씩
        for i in range(0,4): #index: 0~3
            if qs[i] == '-':
                if i == 0:
                    qs[i] = 'java python cpp'
                elif i == 1:
                    qs[i] = 'frontend backend'
                elif i == 2:
                    qs[i] = 'junior senior'
                elif i == 3:
                    qs[i] = 'pizza chicken'
    #[['java', 'backend', 'junior', 'pizza', '100'], 
    # ['python', 'frontend', 'senior', 'chicken', '200'], 
    # ['cpp', 'frontend backend', 'senior', 'pizza', '250'], 
    # ['java python cpp', 'backend', 'senior', 'pizza chiken', '150'], 
    # ['java python cpp', 'frontend backend', 'junior senior', 'chicken', '100'], 
    # ['java python cpp', 'frontend backend', 'junior senior', 'pizza chiken', '150']]

    k = 0
    for qs in query_split:
        for fo in info_split:
            for j in range(0,5):
                if j == 4:
                    if int(fo[j]) >= int(qs[j]):
                        stack[k] += 1
                else:
                    if fo[j] in qs[j]:
                        continue
                    else:
                        break
                
        k += 1

    return stack 
