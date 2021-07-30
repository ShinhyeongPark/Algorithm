# 파이썬
import sys
from collections import deque


def solution(N, road, K):
    nodes = {}
    dist = {i: float('inf') if i != 1 else 0 for i in range(1, N+1)}
    for v1, v2, d in road:
        nodes[v1] = nodes.get(v1, []) + [(v2, d)]
        nodes[v2] = nodes.get(v2, []) + [(v1, d)]
    que = deque([1])

    while que:
        cur_node = que.popleft()
        for nxt_node, d in nodes[cur_node]:
            if dist[nxt_node] > dist[cur_node] + d:
                dist[nxt_node] = dist[cur_node] + d
                que.append(nxt_node)

    return len([True for dist in dist.values() if dist <= K])


# def bfs(g, graph, K, N):
#     q = deque([g])
#     table = [sys.maxsize]*(N+1)
#     table[1] = 0

#     while q:
#         temp = q.popleft()
#         start_point = temp[0]
#         cost = temp[1]

#         for i in graph[start_point]:
#             end_point, new_cost = i[0], i[1]

#             if cost + new_cost <= K and cost + new_cost < table[end_point]:
#                 table[end_point] = cost + new_cost
#                 q.append([end_point, cost+new_cost])

#     return table


# def solution(N, road, K):
#     graph = [[] for _ in range(N+1)]

#     for i, j, cost in road:
#         graph[i].append([j, cost])
#         graph[j].append([i, cost])

#     answer = 0

#     lst = bfs([1, 0], graph, K, N)
#     for i in lst:
#         if i != sys.maxsize:
#             answer += 1

#     return answer
