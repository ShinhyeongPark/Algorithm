# def solution(gems):
#     answer = []

#     n = len(list(set(gems)))

#     for i in range(n, len(gems)+1):
#         for j in range(0, len(gems)-i+1):
#             if len(list(set(gems[j:j+i]))) == n:
#                 answer.append(j+1)
#                 answer.append(j+i)
#                 return answer


def solution(gems): 
    size = len(set(gems)) #집합 -> 중복제거 == 종류의 수
    dic = {gems[0]:1} #딕셔너리 초기 값 : 보석의 첫번째 요소, 1개
    temp = [0, len(gems) - 1] #답이 될 수 있는 후보 
    start , end = 0, 0 #범위의 시작,끝 지점

    while(start < len(gems) and end < len(gems)): #시작,끝 위치가 진열대 길이보다 작을 경우에만 
        if len(dic) == size: #모든 종류의 보석이 딕셔너리에 있을 경우
            if end - start < temp[1] - temp[0]: 
                temp = [start, end]
            
            if dic[gems[start]] == 1: 
                del dic[gems[start]] 
            else: 
                dic[gems[start]] -= 1 
                start += 1 
        else: 
            end += 1 #끝 지점 증가 
            if end == len(gems): 
                break 
            
            if gems[end] in dic.keys(): #이미 딕셔너리에 존재할 경우
                dic[gems[end]] += 1  #값 증가
            else: #딕셔너리에 없을 경우
                dic[gems[end]] = 1 #딕셔너리에 추가
    
    return [temp[0]+1, temp[1]+1]

