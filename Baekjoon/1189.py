import sys


direction = [[-1, 0], [0, 1], [0, -1], [0, 1]]  # 상하좌우 이동

col, row, dis = map(int, sys.stdin.readline().split())  # 행, 렬, 거리제한
count = 0


def dfs(x, y, visit, distance):
    print(x, y)
    global dis
    global count
    visit[x][y] = True
    distance += 1
    print(visit)
    if distance == dis:  # 거리에 도달했을 때
        print("First")
        if x == 0 and y == -1:  # end point에 위치할 경우
            print("Last")
            count += 1
            return
        else:
            return
    else:  # 아직 거리에 도달하지 않았을 경우
        print("Second")
        for direct in direction:
            nx, ny = x + direct[0], y + direct[1]
            # 이동 위치의 좌표값이 인덱스 범위를 벗어날 경우
            if nx < 0 or ny < 0 or nx >= col or ny >= row:
                continue
            print("Third")
            # 유효한 범위에 속할 경우
            if roads[nx][ny] != 'T' and visit[nx][ny] == False:
                dfs(nx, ny, visit, distance)
        return

# start = [-1, 0]  # 좌측 하단(마지막 행 첫번째 열)
# end = [0, -1]  # 우측 상단 (첫번째 행 마지막 열)


roads = []
for _ in range(col):
    tmp = list(sys.stdin.readline().replace('.', 'F').rstrip())
    roads.append(tmp)


visited = [[False] * row for _ in range(col)]
if roads[-1][0] == 'T':  # 시작이 막혀있으면 절대 도달 불가
    print(count)
else:
    dfs(col-1, 0, visited, 0)
    print(count)
