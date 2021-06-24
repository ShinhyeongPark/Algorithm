import sys

N = sys.stdin.readline().rstrip()  # N 입력, N은 구하고자 하는 답의 후보들의 시작값 (13,130,1300)

arrN = list(
    map(int, list(set(list(N.replace('0', '').replace('1', ''))))))
# 0, 1을 없앤 이유는 0으로는 나눗셈이 불가능하고, 1은 무조건 나눠 떨어지기 때문에 불필요한 작업을 없앴다.
# set을 사용해 리스트의 중복을 제거함으로써 불필요한 작업 제거

location = 0  # N에 추가될 자리수
while True:  # 조건이 충족될떄까지 반복
    tmp = int(N + '0' * location)  # N의 자리수를 하나씩 증가 (13,130,1300)

    # 만약 단순히 str(N) in str(tmp)이라고 하면 tmp의 시작위치가 아닌 다른 위치에 포함되어있어도
    # 조건이 참이 되므로 범위를 꼭 정해줘야 한다.
    while str(N) == str(tmp)[:len(str(N))]:  # N이 tmp의 포함되어 있을 경우
        flag = True  # 조건 판단
        for n in arrN:  # 나눌수 : N의 각 자리수
            if tmp % n == 0:  # tmp를 계속 나눔
                continue
            else: #하나라도 나눠떨어지지 않을 경우
                flag = False
                break

        if flag == True:  # 조건에 모두 만족할 경우
            print(tmp) 
            exit() #종료
        else:  
            tmp += 1 #tmp값 증가
    location += 1 #자리수 증가
