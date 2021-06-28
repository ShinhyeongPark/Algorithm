import sys
from collections import deque


def bfs():
    q = deque()
    q.append(N)  # 루트: N

    while q: #K까지 도달할때까지
        x = q.popleft() 

        if x == K: #K 도달
            print(dp[x])
            break
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= MAX and not dp[nx]: #단순이동 또는 순간이동으로 갈 수 있으면
                dp[nx] = dp[x] + 1 #1번 카운팅
                q.append(nx)


MAX = 10 ** 5
dp = [0] * (MAX + 1)
N, K = map(int, sys.stdin.readline().split())

bfs()
