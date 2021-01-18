def solution(n):
    sum = 0
    str1 = str(n)
    answer = sorted(str1, reverse=True)
    answer = [int(i) for i in answer]

    for i in range(0, len(answer)): 
        sum += answer[i] * (10 ** (len(answer) - i-1))
    
    return sum
