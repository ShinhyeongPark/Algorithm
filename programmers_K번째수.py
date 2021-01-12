def solution(array, commands):
    result = []
    answer = []

    for i in range(len(commands)): #0,1,2 3번 반복
        result = array[commands[i][0]-1:commands[i][1]] #2:6
        result.sort()
        answer.append(result[commands[i][2]-1])

    return answer