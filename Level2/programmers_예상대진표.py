def solution(n,a,b):
    people = n #각 라운드에 참가자 수
    round = 1 #라운드
    arr = [0 for j in range(people)] # [0,0,0,0,0,0,0,0]
    a = a - 1 #순서에 -1을 해야 인덱스 값
    b = b - 1 
    arr[a] = 1 #초기 위치 A,B에 1로 지정
    arr[b] = 1 

    while 1:
        for i in range(0,people,2): #두명끼리 반복 
            if arr[i] == 1 and arr[i+1] == 1: #만약 A,B가 같이 있을 경우(만날 경우)
                return round #라운드 반환
        #A,B가 같이 없을 경우
        people = int((people/2)) #참가자 수를 반으로 줄여 다음 라운드 진출
        arr = arr[:people] #참가자 배열을 잘라서 재생성
        for i in range(len(arr)):
            arr[i] = 0
        a = int(a/2) #A,B 위치를 1/2 위치로 초기화
        b = int(b/2)
        arr[a] = 1
        arr[b] = 1
        round += 1 #라운드 증가
