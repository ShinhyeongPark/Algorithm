def solution(n) :
    answer = 0
    lst = [0 for i in range(n)]
    lst[0] = 1
    lst[1] = 2
    for i in range(2, n) :
        lst[i] = (lst[i - 1] + lst[i - 2]) % 1000000007
    answer = lst[n - 1]
    return answer
    
  #- 효율성 문제
	#1. 배열 생성: for문 or *연산
	#2. 경우의 수에 갯수에 따른 효율성 저하: 모든 메모지에이션 계산마다 1000000007계산
  #: 모듈러 연산 -> 큰 수에 대한 체크 
  #결과에 모듈러 연산하는 것이 아니라 연산!에 모듈러 연산
