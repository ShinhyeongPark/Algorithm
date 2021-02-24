T = int(input()) #총 테스트 케이스 수

for t in range(T):
    st = input()[::-1] #거울에 비춰질 문자열
    answer = ""

    for s in st:
        if s == 'b':
            answer += 'd'
        elif s == 'd':
            answer += 'b'
        elif s == 'p':
            answer += 'q'
        elif s == 'q':
            answer += 'p'

    print("#" + str(t+1), answer)
