import heapq
import sys


def dijkstra(start):
    q = []
    distance = [INF] * (v + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node_index, node_cost in graph[now]:
            cost = dist + node_cost

            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))

    return distance


input = sys.stdin.readline
INF = sys.maxsize

v, e, x = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))


result = 0
for i in range(1, v + 1):
    go = dijkstra(i)  # i에서 시작할 때 각 마을까지 최단거리
    back = dijkstra(x)  # 파티 장소에서 시작할때 각 마을까지 최단거리
    result = max(result, go[x] + back[i])

print(result)
