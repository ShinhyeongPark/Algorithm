def solution(n):
    
    answer = 0

    list = str(n)

    for i in range(0, len(str(n))):
        answer +=int(list[i])

    return answer
