import heapq

def minus(n):
    return n * (-1)

def solution(fruitWeights, k):
    answer = set()
    for i in range(0, len(fruitWeights)-k+1):
        tmpList = list(map(minus, fruitWeights[i: i+k]))
        heapq.heapify(tmpList)
        tmp = heapq.heappop(tmpList)
        answer.add(tmp*(-1))
    answer = list(answer)

    answer.sort(reverse=True)
    return answer
