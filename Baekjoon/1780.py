import sys


# def check(x, y, size):
#     global paper
#     pick = table[x][y]
#     # print(x, y)
#     for i in range(x, x + size):
#         for j in range(y, y + size):
#             if pick != table[i][j]:
#                 newSize = size//3
#                 for newi in range(0, 3):
#                     for newj in range(0, 3):
#                         check(i + newi * newSize, j + newj * newSize, newSize)
#                 return

#     paper[pick] += 1


def check(i, j, d):
    global paper
    pick = table[i][j]
    for it in range(i, i+d):
        for jt in range(j, j+d):
            if pick != table[it][jt]:
                newd = d//3
                for mi in range(0, 3):
                    for mj in range(0, 3):
                        check(i + mi*newd, j + mj*newd, newd)
                        return
    paper[pick] += 1


# 0의 갯수, 1의 갯수, -1의 갯수
n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
paper = [0, 0, 0]

check(0, 0, n)
for i in range(-1, 2):
    print(paper[i])

# N = int(sys.stdin.readline())  # Paper Size

# table = [list(map(int, input().split())) for _ in range(N)]

# # print(paper)
# paper = [0, 0, 0]
# check(0, 0, N)

# for i in range(-1, 2):
#     print(paper[i])
