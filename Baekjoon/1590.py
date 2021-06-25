import sys

busNum, arriveTime = map(int, sys.stdin.readline().split())

answer = 2147483648
for n in range(busNum):
    startTime, gap, busCount = map(int, sys.stdin.readline().split())

    while startTime < arriveTime and busCount != 1: # != 0일 경우 buscount+1만큼 반복
        startTime += gap
        busCount -= 1

    # print(startTime)
    if startTime >= arriveTime: # >= 같을 경우에는 0
        answer = min(answer, startTime-arriveTime)

if answer == 2147483648:
    print(-1)
else:
    print(answer)
