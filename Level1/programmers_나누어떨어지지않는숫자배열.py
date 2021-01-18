def solution(arr, divisor):
    answer = []
    arr.sort() #1,2,3,36
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            
    if not answer:
        answer.append(-1)
        return answer
    else:
        return answer
