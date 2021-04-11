import sys
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split()) #노드 수, 간선 수

visit = [0 for i in range(N)] #방문 체크
connection = [] #양방향 연결 리스트
for i in range(N):
    connection.append([0] * N)

for j in range(M):
    x, y = map(int, sys.stdin.readline().split())
    connection[x-1][y-1] = connection[x-1][y-1] = 1

def dfs(x):
    visit[x]= 1
    # connection[x][y] = 0
    # connection[y][x] = 0
    for i in range(N):
        if connection[x][i] == 1 and visit[i] == 0:
            dfs(i)

count = 0
for i in range(N):
    if visit[i] == 0:
        count += 1
        dfs(i)

print(count)

# import sys
# sys.setrecursionlimit(10000)
# n, m = map(int, sys.stdin.readline().split())
# s = [[0] * (n + 1) for i in range(n + 1)]
# visit = [0 for i in range(n + 1)]
# cnt = 0
# def dfs(i):
#     visit[i] = 1
#     for k in range(1, n + 1):
#         if s[i][k] == 1 and visit[k] == 0:
#             dfs(k)
# for i in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     s[a][b] = 1
#     s[b][a] = 1
# for i in range(1, n + 1):
#     if visit[i] == 0:
#         dfs(i)
#         cnt += 1
# print(cnt)
