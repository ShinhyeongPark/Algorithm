import sys
from collections import deque

# [INPUT]
# 6 3
# 1 4 3
# 6 2 5 4
# 2 3

N, M = map(int, input().split())  # N: 가수 인원, M: 각 PD가 정한 가수 인원
adjList = [[]for _ in range(N+1)]  # 인접리스트: A -> B -> C
indegree = [0] * (N+1)  # 가수 X 다음에 올 수 있는 가수의 수

for _ in range(M):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    for node in range(1, tmp[0]):
        adjList[tmp[node]].append(tmp[node+1])
        indegree[tmp[node+1]] += 1
        print('#' + str(tmp[node+1]))

print(adjList)
# [[], [4], [5, 3], [], [3], [4], [2]]
# 1 -> 4
# 2 -> 3,5
# 4 -> 3
# 5 -> 4
# 6 -> 2
print(indegree)  # 첫번째를 제외한 가수가 등장한 수
# [0, 0, 1, 2, 2, 1, 0]

answer = []  # 가능한 가수 순번
queue = deque()

for vertex in range(1, N+1):  # 1~N
    if indegree[vertex] == 0:
        # 💡 indegree가 0일 경우 -> 첫번째 말고 등장한 경우가 없기 때문에 순서 상관없이 앞에 올 수 있다.
        queue.append(vertex)

while queue:  # 큐가 비워질 때까지 반복
    tmp = queue.popleft()  # 큐의 첫번째 원소 추출
    answer.append(tmp)  # answer에 추가

    for nextNode in adjList[tmp]:  # 추추한 vertex와 인접한 노드가 있다면
        indegree[nextNode] -= 1  # 그 인접한 노드의 indegree를 감소
        if indegree[nextNode] == 0:  # 위에 정의한대로 indegree가 0일 경우 큐에 추가
            queue.append(nextNode)

if len(answer) == N:  # 길이가 같다는 것은 순서를 정할 수 있다.
    for order in answer:
        print(order)
else: # 순서를 정할 수 없을 경우
    print(0)
