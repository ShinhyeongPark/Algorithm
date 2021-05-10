def solution(m, n, board):
    result = 0
    block = []
    for bo in board:
        block.append(list(bo))

    while True:
        answer = []
        for i in range(m-1):
            for j in range(n-1):
                if block[i][j] == block[i+1][j] == block[i][j+1] == block[i+1][j+1]:
                    if block[i][j] != 0 and block[i+1][j] != 0 and block[i][j+1] != 0 and block[i+1][j+1] != 0:
                        answer.append([i,j])
                        answer.append([i+1,j])
                        answer.append([i,j+1])
                        answer.append([i+1,j+1])
        
        if len(answer) == 0:
            return result

        temp = []
        for i in answer:
            if i not in temp:
                temp.append(i)
        
        result += len(temp)

        for ans in temp:
            x,y = ans
            block[x][y] = 0

        for i in range(n-1,-1,-1):
            c = []
            for j in range(m-1,-1,-1):
                if block[j][i] != 0:
                    c.append(block[j][i])
            
            for j in range(m-1,-1,-1):
                if len(c) != 0:
                    block[j][i] = c.pop(0)
                else:
                    block[j][i] = 0

