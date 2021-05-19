#[문제해설]
#https://dev-note-97.tistory.com/70
#[내풀이]
# def solution(gems):
#     answer = []

#     n = len(list(set(gems)))

#     for i in range(n, len(gems)+1):
#         for j in range(0, len(gems)-i+1):
#             if len(list(set(gems[j:j+i]))) == n:
#                 answer.append(j+1)
#                 answer.append(j+i)
#                 return answer

#[참고 풀이]
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
#[좋은풀이]
# def solution(gems):
#     answer = [] 
#     shortest = len(gems)+1 # 현재 최단 구간 길이

#     start_p = 0 # 구간의 시작점
#     end_p = 0 # 구간의 끝 점 (보석을 체크하는 기준점)

#     check_len = len(set(gems)) # 보석의 총 종류 수
#     contained = {} # 현재 구간에 포함된 보석들(종류: 갯수)

#     while end_p < len(gems): # 구간의 끝 점이 gems의 길이보다 작을 동안

#         if gems[end_p] not in contained: # 현재 끝 점의 보석이 contained에 없다면(이 종류가 처음 발견되었다면)
#             contained[gems[end_p]] = 1 # dictionary에 추가
#         else:
#             contained[gems[end_p]] += 1 # 이미 있으면 dictionary에 +1
            
#         end_p += 1 # 끝 점 증가

#         if len(contained) == check_len: # 현재 구간 내 보석의 종류의 갯수가 전체 종류의 갯수와 같다면 (현재 구간내 모든 종류가 다 있다면)
#             while start_p < end_p: # start_p 가 end_p 보다 같을 때까지 증가
#                 if contained[gems[start_p]] > 1: # start_p에 해당하는 보석이 구간 내에 하나 이상 있다면
#                     contained[gems[start_p]] -= 1 # 구간 내 보석 하나 감소(start_p 의 보석 뺄거니까)
#                     start_p += 1 # start_p 증가
                    
#                 elif shortest > end_p - start_p: # 기존의 구간 최단거리보다 현재의 구간거리가 더 짧다면
#                     shortest = end_p - start_p
#                     answer = [start_p+1, end_p] # answer와 최단거리 갱신
#                     break
                    
#                 else:
#                     break


#     return answer
