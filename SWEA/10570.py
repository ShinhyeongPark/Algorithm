T = int(input()) #총 테스트 케이스 수

for t in range(1, T+1):
    value = list(map(int, input().split()))
    A = value[0]
    B = value[1]

    count = 0
    for i in range(A, B+1): #1~10
        if str(i) == str(i)[::-1]: #N이 회문인지 판별
            if i ** 0.5 == int(i ** 0.5): #제곱근일 경우
                if str(int(i ** 0.5)) == str(int(i **0.5))[::-1]:
                    count += 1
    print("#" + str(t), count)
