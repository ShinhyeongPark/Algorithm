def solution(d, budget):
    sum = 0
    result = 0
    
    d.sort()
    
    for i in range(len(d)):
        sum += d[i]
        if sum > budget:
            return(result)
        else:
            result += 1
            
    return result
