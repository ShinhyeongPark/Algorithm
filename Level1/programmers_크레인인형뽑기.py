def solution(board, moves):
    answer = []
    bracket = []
    
    
    for v in moves: #열: 1,5,3,5,1,2,1,4
        for i in range(0, len(board)): #열의 제일 위에 원소 찾기: 0~4
            if board[i][v-1] is not 0: #인형이 있을 경우
                if not bracket: #bracket이 비어있을 경우
                    bracket.append(board[i][v - 1])
                    board[i][v - 1] = 0
                    break
                else: #bracket이 채워있을 경우
                    if bracket[len(bracket)-1] == board[i][v - 1]: #같을 경우
                        bracket.pop()
                        answer.append(board[i][v - 1])
                        board[i][v - 1] = 0
                        break
                    else:
                        bracket.append(board[i][v-1])
                        board[i][v - 1] = 0
                        break

    return len(answer) * 2
