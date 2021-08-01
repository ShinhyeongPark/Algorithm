import sys
from collections import deque

N = int(input())
adjList = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
time = [0] * (N+1)

for vertex in range(1, N+1):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))

    time[vertex] = tmp[0]

    for elm in tmp[1:-1]:
        adjList[elm].append(vertex)
        indegree[vertex] += 1
    # order = tmp[1:-1]
    # if order:
    #     order = [vertex] + order
    #     for i in range(len(order)-1):
    #         end, start = order[i], order[i+1]
    #         if end not in adjList[start]:
    #             adjList[start].append(end)
    #             indegree[end] += 1

print(adjList)
print(indegree)
answer = [0] * (N+1)

queue = deque()
for idx in range(1, N+1):
    if indegree[idx] == 0:
        queue.append(idx)
        answer[idx] = time[idx]

#
while queue:
    tmp = queue.popleft()

    # answer[tmp] += time[tmp]

    for nextNode in adjList[tmp]:
        indegree[nextNode] -= 1
        answer[nextNode] = max(answer[nextNode], time[nextNode] + answer[tmp])
        if indegree[nextNode] == 0:
            queue.append(nextNode)

# print(answer)
for i in range(1, N+1):
    print(answer[i])
