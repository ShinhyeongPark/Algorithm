def solution(absolutes, signs):
    answer = 0
    for x, y in zip(absolutes,signs): #zip함수를 사용해 for문에 매개변수를 2개로 한다.
        #x: 정수 값
        #y: 부호(+,-)
        if y == False: #음수
            answer -= x
        else: #양수
            answer += x
    return answer


def main():
    print(solution([4,7,12], [True,False,True]))


main()
