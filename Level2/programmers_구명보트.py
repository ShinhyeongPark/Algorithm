def solution(people, limit):
    p = sorted(people) #List 정렬
    c = 0 #보트 수
    
    while p: #List가 존재할때만 반복
        c += 1
        if len(p) >= 2:
            if p[0] + p[-1] <= limit:
                del p[0]
                del p[-1]
            else:
                del p[-1]
        else:
            del p[0]
            
            
    return c
