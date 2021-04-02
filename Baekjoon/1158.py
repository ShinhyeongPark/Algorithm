N, K = map(int, input().split()) #N:인원 수, K: 삭제 순서

circle = [] #1부터 N까지 사람번호
for i in range(1, N+1):
    circle.append(i) #[1,2,..,N]

answer = [] #요세푸스 순열
start = 0 #Start Location

while circle: #테이블이 없어질때까지 반복
    if not answer: #처음 삽입
        answer.append(str(circle.pop(K-1))) #삭제 후
        start = K - 1 #시작 위치 변경
    else:
        if start > len(circle) - 1: #삭제 위치가 테이블을 벗어났을 경우 = 맨 마지막 원소를 삭제할 경우 
            start = 0 #시작위치를 처음으로 변경
        #시작위치에서 K만큼 이동한 결과가 범위안에 있는지 판단
        if start + (K - 1) > len(circle) - 1: #인덱스 범위를 벗어날 경우
            answer.append(str(circle.pop((start + K - 1) % len(circle))))
            start = (start + K - 1) % (len(circle) + 1)
        else: #범위 안에 있을 경우
            answer.append(str(circle.pop(start + (K - 1))))
            start = start + (K - 1)

print("<%s>" %(", ".join(answer)))
