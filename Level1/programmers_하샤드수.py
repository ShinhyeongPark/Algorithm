def solution(x):
    list = str(x)
    sum = 0

    for i in range(0,len(list)):
        sum += int(list[i])

    if x % sum == 0:
        return True
    else:
        return False
    
    return answer
