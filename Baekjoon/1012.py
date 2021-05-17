import sys
sys.setrecursionlimit(10 ** 5)

def dfs(x,y):
    #다시 탐색하는 것을 방지하기 위해 방분한 위치를 0으로 지정
    arr[x][y] = 0

    #상하좌우
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= M or nx < 0 or ny >= N or ny < 0: #상하좌우의 인덱스가 범위를 벗어날 경우
            continue #pass
        if arr[nx][ny] == 1: #인덱스 범위안에 존재하고, 배추라면
            dfs(nx,ny) #해당 위치에서 탐색


T = int(input()) #테스트 케이스 수

for t in range(T):
    M, N, K = map(int, input().split())
    #M: 행, N: 열, K: 배추 수

    #밭을 표현하는 2차원리스트
    arr = [[0 for n in range(N)] for m in range(M)]

    for k in range(K):
        x, y = map(int, input().split())
        arr[x][y] = 1

    count = 0
    for m in range(M):
        for n in range(N):
            if arr[m][n] == 1: #모여있는 배추의 시작 위치
                count +=1
                dfs(m,n)

    print(count)

