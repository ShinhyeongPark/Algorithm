def solution(n, stages):
    stages.sort() 
    answer = []
    result = []

    for i in range(1, n+1): #1라운드부터 5라운드까지
        if stages.count(i) == 0:
            answer.append(0)
        else:
            answer.append(stages.count(i) / len(stages))
            while 1:
                if i in stages:
                    stages.remove(i)
                else:
                    break

    for v in range(len(answer)):
        result.append(answer.index(max(answer))+1)
        answer[answer.index(max(answer))] = -1

    return result
