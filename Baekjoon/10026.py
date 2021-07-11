import sys


def dfsA(x, y, color):
    global sectionA
    sectionA[x][y] = '0'

    if x + 1 < N and sectionA[x+1][y] == color:
        dfsA(x+1, y, color)

    if y + 1 < N and sectionA[x][y+1] == color:
        dfsA(x, y+1, color)

    if x - 1 >= 0 and sectionA[x-1][y] == color:
        dfsA(x-1, y, color)

    if y - 1 >= 0 and sectionA[x][y-1] == color:
        dfsA(x, y-1, color)


def dfsB(x, y, color):
    global sectionB
    sectionB[x][y] = '0'

    if x + 1 < N and sectionB[x+1][y] == color:
        dfsB(x+1, y, color)

    if y + 1 < N and sectionB[x][y+1] == color:
        dfsB(x, y+1, color)

    if x - 1 >= 0 and sectionB[x-1][y] == color:
        dfsB(x-1, y, color)

    if y - 1 >= 0 and sectionB[x][y-1] == color:
        dfsB(x, y-1, color)


N = int(sys.stdin.readline())


sectionA = []
sectionB = []
for _ in range(N):
    tmp = sys.stdin.readline().rstrip()
    A = list(tmp)
    B = list(tmp.replace('R', 'G'))

    sectionA.append(A)
    sectionB.append(B)

countA = 0
countB = 0
for x in range(N):
    for y in range(N):
        if sectionA[x][y] != '0':
            countA += 1
            dfsA(x, y, sectionA[x][y])

for x in range(N):
    for y in range(N):
        if sectionB[x][y] != '0':
            countB += 1
            dfsB(x, y, sectionB[x][y])

print(countA, countB)
# print(countB)
