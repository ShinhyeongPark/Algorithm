# BFS
from collections import deque


def solution(maps):
    # 좌표 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 지도의 크기
    row = len(maps)
    col = len(maps[0])
    # 각 위치까지 거리를 저장하기 위한 리스트
    graph = [[-1 for _ in range(col)] for _ in range(row)]

    queue = deque()
    queue.append([0, 0])  # 시작점 (0,0)

    graph[0][0] = 1  # 시작위치의 값은 1

    while queue:
        y, x = queue.popleft()  # 도달 가능한 좌표를 차례대로 탐색

        for idx in range(4):
            ny = y + dy[idx]
            nx = x + dx[idx]

            #범위에 속하고, 벽이 아닐 경우
            if 0 <= ny < row and 0 <= nx < col and maps[ny][nx] == 1:
                # 아직 탐색하지 않은 곳일 경우
                if graph[ny][nx] == -1:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append([ny, nx])

    return graph[-1][-1]


def main():
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
          1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]	))


main()
