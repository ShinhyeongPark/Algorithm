def solution(prices):
    #prices = [1, 2, 3, 2, 3]
    answer = []

    for i in range(0, len(prices)): #i: 4
        count = 0
        for j in range(i+1, len(prices)): #j: 5~4
            if j == len(prices)-1:
                #print(count)
                answer.append(count+1)
            elif prices[i] > prices[j]:
                #print(count)
                answer.append(count+1)
                break
            else:
                count += 1

    answer.append(0)
    return answer
