N = int(input())

#1과 N+1 사이에 수를 자리수로 나눠 저장
bp = []
for i in range(1, N+1):
    bp.append(list(map(int, list(str(i)))))

count = 0
for x in bp:
    flag = 1
    if len(x) == 1 or len(x) == 2: #한자리수, 두자리수일 경우는 등차수열이 적용이 되지 않음
        count += 1
    else:
        diff = x[1] - x[0] #처음 연속된 수의 차이를 저장
        for i in range(1, len(x)-1): #각 위치에서의 차이를 계산
            if x[i+1] - x[i] != diff: #diff와 다를 경우는 등차수열 성립 깨짐
                flag = 0
                break

        if flag == 1: #3자리수 이상 수중 등차수열을 이룰 경우
            count += 1

print(count)
