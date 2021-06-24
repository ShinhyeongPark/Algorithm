import sys

N, M = map(int, sys.stdin.readline().split())

light = []
for n in range(N):
    light.append(sys.stdin.readline())

K = int(sys.stdin.readline())

maxCount = 0  # Answer

for col1 in range(N):
    zeroCount = 0
    for num in light[col1]:  # 각 행의 포함된 0의 개수 계산
        if num == '0':
            zeroCount += 1

    lightCount = 0
    if zeroCount <= K and zeroCount % 2 == K % 2:
        for col2 in range(N):
            if light[col1] == light[col2]:
                lightCount += 1

    maxCount = max(maxCount, lightCount)

print(maxCount)
