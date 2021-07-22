import sys

go = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
# 좌표에서 모든방향으로 인접한 좌표 위치


def dfs(x, y):
    global isPeak
    for g in go:  # 모든 방향 탐색
        nx, ny = x + g[0], y + g[1]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:  # 인덱스 범위를 벗어날 경우 pass
            continue
        if mount[x][y] < mount[nx][ny]:
            isPeak = False
        # 이미 방문한거면 탐색을 넘어가고, 방문은 하지 않았지만
        if visited[nx][ny] == True or mount[x][y] != mount[nx][ny]:
            continue

        visited[nx][ny] = True
        dfs(nx, ny)

    return


N, M = map(int, sys.stdin.readline().split())  # 행(x증가)/열(y증가)

mount = []  # 각 좌표의 높이
for _ in range(N):
    mount.append(list(map(int, sys.stdin.readline().rstrip().split())))

isPeak = True  # 해당 좌표가 봉우리일 경우
countPeak = 0  # 총 봉우리 개수
visited = [[False] * M for _ in range(N)]  # DFS 탐색을 위한 방문확인

for i in range(N):
    for j in range(M):
        if visited[i][j] == False:
            isPeak = True
            dfs(i, j)
            if isPeak:
                countPeak += 1


print(countPeak)
