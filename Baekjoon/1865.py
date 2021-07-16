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

#Bellman-Ford 참고
# import sys

# input = sys.stdin.readline
# INF = int(1e9)


# # 벨만 포드 알고리즘
# def bf(start):
#     dis = [INF] * (n+1)  # 최단거리 초기화
#     dis[start]=0
#     # 메인 로직
#     # 음의 사이클 판별을 위해 n-1번이 아닌 n번 반복
#     for i in range(n):
#         # 반복마다 모든 간선 확인
#         for edge in edges:
#             cur = edge[0] # 출발
#             next_node = edge[1] # 도착
#             cost = edge[2] # 비용

#             # 현재 노드에 도달이 가능하면서
#             # 다음 노드로 이동하는 거리가 최단거리로 갱신가능한 경우
#             if dis[cur] != INF and dis[next_node] > cost + dis[cur]:
#                 dis[next_node] = cost + dis[cur]
#                 # i==n-1이면 n번 돌린건데 이때도 갱신이 발생하면 음의 싸이클 존재
#                 if i == n - 1:
#                     return True

#     return False


# t = int(input())

# for _ in range(t):
#     # 지점수, 도로수, 웜홀수
#     n, m, w = map(int, input().split())
#     edges = []

#     # 도로 정보
#     for _ in range(m):
#         s, e, t = map(int, input().split())
#         edges.append((s, e, t))
#         edges.append((e, s, t))

#     # 웜홀 정보
#     for _ in range(w):
#         s, e, t = map(int, input().split())
#         edges.append((s, e, -t))

#     key=0
#     for i in range(1,n+1):
#         if bf(i):
#             key=1
#             break
#     if key:
#         print("YES")
#     else:
#         print("NO")
