def solution(n, times):
    times.sort()  # 이분탐색을 위한 정렬

    minTime = 1  # 심사관 1명의 1분 걸릴 경우
    maxTime = n * times[-1]  # n명의 심사관 중 가장 긴 시긴

    answer = maxTime

    while minTime <= maxTime:  # min이 max보다 커질 때까지 이분탐색
        midTime = int((minTime + maxTime) / 2)  # 중앙값 탐색

        person = 0

        for i in range(len(times)):
            person += int(midTime/times[i])  # 중앙값일 때 심사가능한 인원

        print(person, n, midTime, maxTime, minTime)
        if person >= n:  # 중앙값일 때 심사받을 수 있는 인원이 n보다 클 경우
            if answer > midTime:
                answer = midTime

            maxTime = midTime - 1
        else:
            minTime = midTime + 1

    return answer


def main():
    print(solution(6, [7, 10]))


main()
