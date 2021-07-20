# import sys

# goX = [-1, -1, 1, 1]  # 행 이동
# goY = [-1, 1, -1, 1]  # 열 이동


# def catch(x, y):
#     step = 1
#     while x + step < N:
#         if y - step >= 0 and maps[x+step][y-step] == 1:
#             maps[x+step][y-step] = 0
#         if y + step < N and maps[x+step][y+step] == 1:
#             maps[x+step][y+step] = 0
#         step += 1

#     step = 1
#     while x - step >= 0:
#         if y - step >= 0 and maps[x - step][y-step] == 1:
#             maps[x-step][y-step] = 0
#         if y + step < N and maps[x - step][y+step] == 1:
#             maps[x-step][y+step] = 0
#         step += 1


# N = int(input())

# maps = []
# for _ in range(N):
#     maps.append(list(map(int, sys.stdin.readline().rstrip().split())))

# count = 0
# for x in range(N):
#     for y in range(N):
#         if maps[x][y] == 1:
#             catch(x, y)
#     # count += maps[x].count(1)

# # print(count)
# # print(maps)
# for m in maps:
#     count += m.count(1)

# print(count)
n = int(input())  # 체스판 크기

chess_map = []  # 체스판
# 검은색/흰색 칸 위치에 있는 비숍은 서로 영향을 주지 않기 때문에
# 이를 분리하여 효율성을 증가
black = []  # 비숍이 놓일 수 있는(1) 검은색의 좌표
white = []  # 비숍이 놓일 수 있는(1) 흰색의 좌표

# 체스판을 색깔로 구분
# 검은칸:1 , 흰색칸:0
color = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        color[i][j] = (i % 2 == 0 and j % 2 == 0) or (i %
                                                      2 != 0 and j % 2 != 0)
# color (True: 검/ False: 흰)
#[[True, False, True, False, True], [False, True, False, True, False], [True, False, True, False, True], [False, True, False, True, False], [True, False, True, False, True]]

for i in range(n):
    chess_map.append(list(map(int, input().split())))
    for j in range(n):
        # True가 검은색
        # 비숍이 놓일 수 있는 위치이고 검은색일 경우
        if chess_map[i][j] == 1 and color[i][j] == 1:
            black.append((i, j))
        # False가 흰색
        # 비숍이 놓일 수 있는 위치이고 흰색일 경우
        if chess_map[i][j] == 1 and color[i][j] == 0:
            white.append((i, j))

# 검은색인 경우
Bcnt = 0
# 흰색인 경우
Wcnt = 0

isused01 = [0]*(n*2-1)  # 좌하강 대각선
isused02 = [0]*(n*2-1)  # 우하강 대각선

# print(black)
# [(0, 0), (0, 4), (1, 1), (2, 0), (2, 2), (2, 4), (4, 0), (4, 2), (4, 4)]
# print(white)
# [(0, 1), (0, 3), (3, 0), (4, 3)]

# fun(색깔, 검/흰일 때 비숍의 좌표, 갯수)


def fun(bishop, index, count):
    global Bcnt, Wcnt
    if index == len(bishop):  # 마지막 위치에 도착할 경우
        rx, ry = bishop[index-1]  # ex) 0,0 / 0,4 / 1,1
        # 블랙이면 Bcnt 최대값
        if color[rx][ry]:  # True -> 검
            Bcnt = max(Bcnt, count)
        # 흰색이면 Wcnt 최대값
        else:  # False -> 흰
            Wcnt = max(Wcnt, count)
        return

    x, y = bishop[index]
    if isused01[x+y] or isused02[x-y+n-1]:
        fun(bishop, index+1, count)
    else:
        isused01[x+y] = 1
        isused02[x-y+n-1] = 1
        fun(bishop, index+1, count+1)
        isused01[x+y] = 0
        isused02[x-y+n-1] = 0
        fun(bishop, index+1, count)


# 색깔별로 탐색 (가장 핵심)
if len(black) > 0:  # 검은색 판에 비숍이 하나라도 놓일 수 있을 경우
    fun(black, 0, 0)
if len(white) > 0:  # 흰색 판에 비숍이 하나라도 놓일 수 있을 경우
    fun(white, 0, 0)
print(Bcnt+Wcnt)
