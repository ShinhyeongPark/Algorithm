def solution(rows, columns, queries):
    answer = []  # 각 회전마다 최소값을 저장할 리스트

    # 1부터 순차적으로 증가하는 rows x columns 크기의 리스트
    arr = []
    for i in range(0, rows):  # 행
        tmp = [i * columns + j for j in range(1, columns+1)]
        arr.append(tmp)

    # 회전 시작
    for query in queries:
        # (x1,y1) (x2,y2)
        x1, y1, x2, y2 = query[0], query[1], query[2], query[3]

        # 회전의 시작좌표이자 회전시 최소값을 구하기 위한 초기값
        minIndex = arr[x1-1][y1-1]

        # 업데이트를 위한 다음 인덱스 값을 저장할 변수
        tmp = minIndex
        # Right
        for i in range(y2-y1):
            nextTmp = arr[x1-1][y1 + i]
            if minIndex > nextTmp:
                minIndex = nextTmp
            arr[x1-1][y1 + i] = tmp
            tmp = nextTmp

        # Down
        for i in range(x2-x1):
            nextTmp = arr[x1 + i][y2-1]
            if minIndex > nextTmp:
                minIndex = nextTmp
            arr[x1 + i][y2-1] = tmp
            tmp = nextTmp

        # Left
        for i in range(y2-y1):
            nextTmp = arr[x2-1][y2 - i - 2]
            if minIndex > nextTmp:
                minIndex = nextTmp
            arr[x2-1][y2 - i-2] = tmp
            tmp = nextTmp

        # Up
        for i in range(x2-x1):
            nextTmp = arr[x2 - i - 2][y1-1]
            if minIndex > nextTmp:
                minIndex = nextTmp
            arr[x2 - i - 2][y1-1] = tmp
            tmp = nextTmp

        answer.append(minIndex)
    return answer
