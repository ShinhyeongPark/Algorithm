import sys


def dfs(start):
    visit[start] = True
    dfsArr.append(start)

    for next in range(1, N+1):
        if visit[next] == False and next in graph[start]:
            dfs(next)


def bfs(start):
    queue = [start]
    visit[start] = False

    while queue:
        start = queue[0]
        bfsArr.append(queue[0])
        del queue[0]

        for next in range(1, N+1):
            if visit[next] == True and next in graph[start]:
                queue.append(next)
                visit[next] = False


N, E, S = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
visit = [False] * (N+1)

# 노드 크기가 작은것 부터
for _ in range(E):
    start, end = map(int, sys.stdin.readline().split())

    graph[start].append(end)
    graph[end].append(start)

dfsArr = []
bfsArr = []

dfs(S)
bfs(S)

print(' '.join(list(map(str, dfsArr))))
print(' '.join(list(map(str, bfsArr))))
