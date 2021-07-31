import sys
from collections import deque

T = int(input())  # Test Case Count

for _ in range(T):
    # N: 총 빌딩 수, K: 총 규칙 수
    N, K = map(int, sys.stdin.readline().rstrip().split())
    # 각 빌딩을 짓는데 걸리는 시간
    time = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    # 인덱스와 건물 번호를 맞추기 위해 맨 앞에 [0]을 추가
    adjList = [[] for _ in range(N+1)]  # 인접리스트
    indegree = [0] * (N+1)  # 진입차수
    dp = [0] * (N+1)  # 위상정렬을 사용해야하지만, 이전 문제와 다르게 총 걸린 시간을 구해야 되기 때문에
    # DP 사용

    for _ in range(K):
        start, end = map(int, sys.stdin.readline().rstrip().split())
        adjList[start].append(end)  # start → end
        indegree[end] += 1  # end 노드로 들어오는 진입차수
        # 진입차수가 0인 것을 구해 그 노드부터 시작

    lastBuilding = int(input())  # 마지막으로 지을 건물

    queue = deque()
    # 진입차수가 0인 노드 계산
    for vertex in range(1, N+1):
        if indegree[vertex] == 0:
            queue.append(vertex)
            dp[vertex] = time[vertex]

    while queue:
        previousNode = queue.popleft()
        for nextNode in adjList[previousNode]:
            indegree[nextNode] -= 1  # 진입차수 감소
            # nextNode를 짓는데 걸린 시간과 previousNode를 짓는데 걸린 시간 + nextNode를 짓는데 필요한 시간을 비교
            dp[nextNode] = max(dp[nextNode], dp[previousNode] + time[nextNode])
            if indegree[nextNode] == 0:  # 진입차수가 0이 되면,
                queue.append(nextNode)  # 큐에 추가

    print(dp[lastBuilding])
