from itertools import combinations #조합 사용

def solution(orders, course):
    stack = [] #주문문자열을 리스트로 변환, 스택을 사용한다.
    answer = [] #코스요리 구성(정렬된 후 반환) 

    for v in orders:
        stack.append(sorted(list(v)))
        #만약 stack.append(list(v))라고 할 경우
        #WX와 XW를 다른 메뉴 구성으로 보기 때문에 정렬한 값을 스택에 저장해야 한다.

    for i in course: #course만큼 반복
        combs = [] #조합 개수에 따라 Update할 List
        count = {} #코스 구성의 중복 개수
        for j in range(len(stack)): #코스구성만큼
            for k in combinations(stack[j],i):
                combs.append(''.join(list(k))) #주문목록에서 가능한 조합을 저장
        
        #중복원소 계산
        #count: Dict
        for comb in combs:
            try: count[comb] += 1
            except: count[comb] = 1

        for x in count:
            #문제 조건에 2명이상이 주문해야 하므로 max값이 1보다 크다는 조건을 줘야한다.
            if max(count.values()) > 1:
                if count[x] == max(count.values()):
                    answer.append(x)
    
    return sorted(answer)
