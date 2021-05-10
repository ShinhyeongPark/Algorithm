def solution(m, n, board):
    result = 0
    block = []
    for bo in board:
        block.append(list(bo))

    while True: #2x2블록이 없을떄까지 반복
        answer = []
        for i in range(m-1):
            for j in range(n-1):
                if block[i][j] == block[i+1][j] == block[i][j+1] == block[i+1][j+1]: #0이 아닌 문자로 이뤄진 2x2 블록
                    if block[i][j] != 0 and block[i+1][j] != 0 and block[i][j+1] != 0 and block[i+1][j+1] != 0:
                        answer.append([i,j])
                        answer.append([i+1,j])
                        answer.append([i,j+1])
                        answer.append([i+1,j+1])
        
        if len(answer) == 0: #추가적인 블록이 없다? -> 2x2 블록이 없다.
            return result #총 사라진 블럭 수 리턴

        temp = [] #중복 제거를 위한 리스트
        for i in answer:
            if i not in temp:
                temp.append(i)
        result += len(temp)

        for ans in temp: #사라진 블럭은 0으로 변환
            x,y = ans
            block[x][y] = 0

        #열을 기준으로 비교하며 계속해서 교환
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

def main():
    print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

main()
