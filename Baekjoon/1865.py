import sys
# sys.setrecursionlimit(10**7)


def solution(startPoint, start, time, visit):
    global flag
    visit[start] = True
    # print(visit)
    for end in range(N+1):
        if routes[start][startPoint] != 0:
            # print(2, routes[start][startPoint])
            if time + routes[start][startPoint] < 0:
                flag = True
                # print("END")
                # return 0

        if routes[start][end] != 0 and visit[end] == 0:
            # print(1, routes[start][end])
            solution(startPoint, end, time + routes[start][end], visit)
        else:
            continue


T = int(input())

for _ in range(T):
    N, M, W = map(int, sys.stdin.readline().rstrip().split())

    routes = [[0] * (N+1) for _ in range(N+1)]

    for _ in range(M):
        start, end, time = map(int, sys.stdin.readline().rstrip().split())
        routes[start][end] = time

    for _ in range(W):
        start, end, time = map(int, sys.stdin.readline().rstrip().split())
        routes[start][end] = -time

    # global flag
    flag = False
    for start in range(1, N+1):
        # print("시작위치:" + str(start))
        time = 0
        visit = [False] * (N+1)
        solution(start, start, time, visit)

    if flag == True:
        print("YES")
    else:
        print("NO")
