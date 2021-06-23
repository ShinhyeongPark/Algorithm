import sys
import heapq

N, M = map(int, sys.stdin.readline().split())  # N: 문제 수, M: 먼저 풀어야 문제의 수
# 연결된 문제
order = [[] for _ in range(N+1)]  # [[], [], [], [], []]
# 연결된 문제 연결 수
linked = [0 for _ in range(N+1)]  # [0,0,0,0,0]

heap = []
result = []  # 최종 문제 풀이의 순서

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())  # x가 y보다 먼저 풀어야됨
    order[x].append(y)  # 4 -> 2, 3 -> 1
    linked[y] += 1  # 연결 수 증가

for i in range(1, N+1):  # 우선 연결 문제가 아닌 문제들의 번호를
    if linked[i] == 0:
        heapq.heappush(heap, i)  # heap에 저장

while heap:
    n = heapq.heappop(heap)  # 힙의 최소값 추출
    result.append(n)  # result에 저장

    for i in order[n]:  # n에 대해 연결된 문제가 있을 경우
        linked[i] -= 1

        if linked[i] == 0:
            heapq.heappush(heap, i)

print(*result)
