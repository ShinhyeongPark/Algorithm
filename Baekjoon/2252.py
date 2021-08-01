from collections import deque

N, K = map(int, input().split())
indegree = [0] * (N+1)
adjList = [[] for _ in range(N+1)]

# 인접리스트 생성
for _ in range(K):
    start, end = map(int, input().split())

    adjList[start].append(end)
    # 진입차수 증가
    indegree[end] += 1

# print(adjList)
# print(indegree)

queue = deque()
#진입차수가 0인 vertex를 queue에 추가
for idx in range(1, N+1):
    if indegree[idx] == 0:
        queue.append(idx)

# print(queue)
answer = [] #줄을 세웠을 때 순서
while queue:
    tmp = queue.popleft()
    answer.append(tmp)

    for nextNode in adjList[tmp]:
        indegree[nextNode] -= 1
        if indegree[nextNode] == 0:
            queue.append(nextNode)

if len(answer) == N:
    print(' '.join(map(str, answer)))
