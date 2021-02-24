T = int(input()) #총 테스트 케이스 수

#여러 번의 반복을 해야되기 때문에
#시간 복잡도를 고려하여, 조건이 한번이라도 만족하지 않을 겨웅
#바로 Break!

for t in range(T):
    flag = True #flag가 False일 경우 스도쿠 조건 만족 X -> 0 출력 후 종료
    sudoku = []
    for i in range(9): #9X9만큼 반복
        sudoku.append(list(map(int, input().split())))

    for sudo in sudoku: #같은 행 합
        if sum(sudo) != 45:
            flag = False
            break

    if flag == False:
        print("#" + str(t+1), "0")
    else:
        for j in range(9): #같은 열 합
            stack_sum = 0 
            for k in range(9):
                stack_sum += sudoku[k][j]

            if stack_sum != 45:
                flag = False
                break

        if flag == False:
            print("#" + str(t+1), "0")
        else: #3X3 조건 
            for x in range(0,7,3):
                nine_sum = 0
                for y in range(0,7,3):
                    nine_sum = sudoku[x][y] + sudoku[x][y+1] + sudoku[x][y+2] + sudoku[x+1][y] + sudoku[x+1][y+1] + sudoku[x+1][y+2] + sudoku[x+2][y] + sudoku[x+2][y+1] + sudoku[x+2][y+2] 
                    if nine_sum != 45:
                        flag = False
                        break
                    else:
                        nine_sum = 0
                if flag == False:
                    print("#" + str(t+1), "0")
                    break
            if flag == True:
                print("#" + str(t+1), "1")
                
