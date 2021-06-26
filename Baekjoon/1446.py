import sys
# N: route number, D: road distance
N, D = map(int, sys.stdin.readline().split())

routes = []  # route case
for n in range(N):
    start, end, length = map(int, sys.stdin.readline().split())

    if start > D or end > D:  # if route's end point exceeed Distance
        continue
    elif end - start < length:  # gap in start and end longer than road length
        continue
    else:
        routes.append([start, end, length])


position = [i for i in range(D+1)]
for j in range(D+1):  # road의 각 위치에서 체크
    if j != 0:
        # 위치 j = 위치 j와 위치 j 이전 위치에 1 큰 것 중 최소
        position[j] = min(position[j], position[j-1]+1)
    for route in routes:
        if route[0] == j:  # 만약 지름길중 시작위치가 위치 j일 경우
            position[route[1]] = min(
                position[route[1]], position[route[0]] + route[2])
            # 지름길의 끝지점은 길의 끝지점과 길의 시작위치에서 지름길 길이만큼 더한 것중 최소
print(position)
print(position[D])

# INPUT
# 5 150
# 0 50 10
# 0 50 20
# 50 100 10
# 100 151 10
# 110 140 90
