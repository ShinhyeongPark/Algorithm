import sys

N = int(input())  # 마을 수
M = int(input())  # 버스 수
INF = sys.maxsize  # 최소값을 구하기 위한 비교 대상(최대로 지정)

#i/j 행렬이 있을 때 i->j로 이동하는 경로
routes = [[INF] * N for _ in range(N)] #Max로 채워진 2차원 배열
for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())

    #만약 동일한 노선이 있을 경우 더 작은 값을 저장
    if routes[start-1][end-1] > cost:
        routes[start-1][end-1] = cost

for temp in range(N): #temp: start와 end사이에의 거쳐갈 수 있는 정류장
    for start in range(N):
        for end in range(N):
            if routes[start][end] > routes[start][temp] + routes[temp][end] and start != end:
                routes[start][end] = routes[start][temp] + routes[temp][end]

for route in routes:
    for r in route:
        if r == INF:
            print(0, end=' ')
        else:
            print(r, end=' ')
    print()
