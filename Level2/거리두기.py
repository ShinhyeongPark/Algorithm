dxdy = [[1, -1], [1, 0], [2, 0], [1, 1], [0, 1], [0, 2]]


def covid(place):
    for x in range(5):
        for y in range(5):
            if place[x][y] == 'P':
                # 현재 위치가 P일 때만 판단
                for d in dxdy:  # 멘헤튼 거리 판단
                    if 0 <= x + d[0] < 5 and 0 <= y + d[1] < 5:  # 인덱스 범위 체크
                        # print("T1")
                        # print(x+d[0], y+d[1])
                        if place[x + d[0]][y + d[1]] == 'P':  # P에서 멘헤튼 거리안에 P'가 존재할 경우
                            # print("T2")
                            # P' == P[x+1][y+1]
                            if d[0] == 1 and d[1] == -1:
                                if place[x+1][y] == 'X' and place[x][y-1] == 'X':
                                    continue
                                else:
                                    # print(1)
                                    # print(x, y)
                                    return 0
                            if d[0] == 1 and d[1] == 1:
                                if place[x+1][y] == 'X' and place[x][y+1] == 'X':
                                    continue
                                else:
                                    # print(2)
                                    # print(x, y)
                                    return 0
                            elif d[0] == 2 and d[1] == 0:
                                if place[x+1][y] == 'X':
                                    continue
                                else:
                                    # print(3)
                                    # print(x, y)
                                    return 0
                            elif d[0] == 0 and d[1] == 2:
                                if place[x][y+1] == 'X':
                                    continue
                                else:
                                    # print(4)
                                    # print(x, y)
                                    return 0
                            else:
                                return 0
    return 1


def solution(places):
    answer = []

    for place in places:  # ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]
        answer.append(covid(place))

    return answer
