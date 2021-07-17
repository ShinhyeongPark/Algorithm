import sys


def dfs(start, visit, item, dis):
    visit[start] = True
    item += T[start]

    if roads[start]:
        for next in roads[start]:
            if next[1] + dis < M and visit[next[0]] == False:
                item += dfs(next[0], visit, 0, next[1] + dis)
    else:
        return item

    return item


N, M, R = map(int, sys.stdin.readline().split())

T = [0] + list(map(int, sys.stdin.readline().split()))

roads = [[] for _ in range(N+1)]

for _ in range(R):
    start, end, cost = map(int, sys.stdin.readline().split())

    roads[start].append([end, cost])
    roads[end].append([start, cost])

itemCount = 0
for startNode in range(1, N+1):
    visited = [False] * (N+1)
    itemCount = max(itemCount, dfs(startNode, visited, 0, 0))

print(itemCount)


#다익스트라 말고 워셜 플루이드로 풀이 방식
# INF = int(1e9)

# N, M, R = map(int, input().split())
# area_item = list(map(int, input().split()))
# arr = [[INF] * N for _ in range(N)]

# for _ in range(R):
#     start, end, dist = map(int, input().split())
#     arr[start-1][end-1] = min(arr[start-1][end-1], dist)
#     arr[end-1][start-1] = min(arr[end-1][start-1], dist)

# for k in range(N):
#     for a in range(N):
#         for b in range(N):
#             arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])
#             if a == b:
#                 arr[a][b] = 0

# max_value = 0

# for i in range(N):
#     temp_value = 0
#     for j in range(N):
#         if arr[i][j] <= M:
#             temp_value += area_item[j]

#     max_value = max(max_value, temp_value)

# print(max_value)
