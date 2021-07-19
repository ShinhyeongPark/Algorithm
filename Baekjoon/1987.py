import sys

go = [[0, -1], [0, 1], [-1, 0], [1, 0]]


def dfs(x, y, dis):  # 행, 열
    dis.append(board[x][y])

    global maxDis
    maxDis = max(maxDis, len(dis))

    for g in go:
        if 0 <= y + g[0] < C and 0 <= x + g[1] < R and board[x + g[1]][y + g[0]] not in dis:
            dfs(x + g[1], y + g[0], dis)
            dis.remove(board[x + g[1]][y + g[0]])


R, C = map(int, sys.stdin.readline().split())

board = []
for _ in range(R):
    board.append(list(sys.stdin.readline().rstrip()))

dis = []
maxDis = 0
dfs(0, 0, [])

print(maxDis)
