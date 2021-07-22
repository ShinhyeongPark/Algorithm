import sys

N = int(input())

schedule = []
for _ in range(N):
    time, limit = map(int, sys.stdin.readline().rstrip().split())

    schedule.append([time, limit])

schedule = sorted(schedule, key=lambda x: -x[1])

nowTime = schedule[0][1]
for i in range(N-1):
    nowTime -= schedule[i][0]

    if nowTime <= schedule[i+1][1]:
        continue
    else:
        nowTime = schedule[i+1][1]

nowTime -= schedule[-1][0]
if nowTime < 0:
    print(-1)
else:
    print(nowTime)
