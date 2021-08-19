from collections import deque


def can_rotate(y1, x1, y2, x2, board, flag):  # 회전이 가능한지
    n = len(board)
    if y1 == y2:  # 가로인 경우
        if x1 > x2:
            ly, lx, ry, rx = y1, x1, y2, x2
        else:
            ly, lx, ry, rx = y2, x2, y1, x1

        if flag == 'r':  # 오른쪽 축일 경우
            if ly+1 < n and board[ly+1][lx] == 0 and board[ly+1][rx] == 0:
                return ry, rx, ry+1, rx
        else:  # 왼쪽 축일 경우
            if ly-1 >= 0 and board[ly-1][rx] == 0 and board[ly-1][rx] == 0:
                return ly-1, lx, ly, lx

    else:  # 세로인 경우
        if y1 > y2:
            uy, ux, dy, dx = y1, x1, y2, x2
        else:
            uy, ux, dy, dx = y2, x2, y1, x1

        if flag == 'u':
            if dx+1 < n and board[uy][dx+1] == 0 and board[dy][dx+1] == 0:
                return uy, ux, uy, ux+1
        else:
            if dx-1 >= 0 and board[dy][dx-1] == 0 and board[dy][uy][dx-1] == 0:
                return dy, dx-1, dy, dx

    return -1, -1, -1, -1


def solution(board):
    #[[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
    answer = 0
    dely, delx = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    q.append([[0, 0], [0, 1], 0])
    n = len(board)
    visit = set([((0, 0), (0, 1))])
    print(visit)
    while q:
        info = q.popleft()

        ly, lx, ry, rx, time = info[0][0], info[0][1], info[1][0], info[1][1], info[2]

        if (ly == n-1 and lx == n-1) or (ry == n-1 and rx == n-1):
            return time
        for i in range(4):

            nly, nlx, nry, nrx = ly+dely[i], lx+delx[i], ry+dely[i], rx+delx[i]
            if 0 <= nly < n and 0 <= nlx < n and 0 <= nry < n and 0 <= nrx < n:  # 왼쪽, 오른쪽 모두 이동 가능할 경우
                if board[nly][nlx] == 0 and board[nry][nrx] == 0 and ((nly, nlx), (nry, nrx)) not in visit:
                    q.append([[nly, nlx], [nry, nrx], time+1])
                    visit.add(((nly, nlx), (nry, nrx)))

        if ly == ry:
            if can_rotate(nly, nlx, nry, nrx, board, 'r')[0] != -1 and ((nly, nlx), (nry, nrx)) not in visit:
                nly, nlx, nry, nrx = can_rotate(nly, nlx, nry, nrx, board, 'r')
                q.append([[nly, nlx], [nry, nrx], time+1])
                visit.add(((nly, nlx), (nry, nrx)))
            if can_rotate(nly, nlx, nry, nrx, board, 'l')[0] != -1 and ((nly, nlx), (nry, nrx)) not in visit:
                nly, nlx, nry, nrx = can_rotate(nly, nlx, nry, nrx, board, 'l')
                q.append([[nly, nlx], [nry, nrx], time+1])
                visit.add(((nly, nlx), (nry, nrx)))

        else:
            if can_rotate(nly, nlx, nry, nrx, board, 'u')[0] != -1 and ((nly, nlx), (nry, nrx)) not in visit:
                nly, nlx, nry, nrx = can_rotate(nly, nlx, nry, nrx, board, 'u')
                q.append([[nly, nlx], [nry, nrx], time+1])
                visit.add(((nly, nlx), (nry, nrx)))
            if can_rotate(nly, nlx, nry, nrx, board, 'd')[0] != -1 and ((nly, nlx), (nry, nrx)) not in visit:
                nly, nlx, nry, nrx = can_rotate(nly, nlx, nry, nrx, board, 'd')
                q.append([[nly, nlx], [nry, nrx], time+1])
                visit.add(((nly, nlx), (nry, nrx)))

    return answer


def main():
    print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
          0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))


main()
