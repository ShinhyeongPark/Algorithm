def solution(brown, yellow):
    answer = []
    result = brown + yellow
    
    garo = 0
    sero = 0
    for i in range(1, result+1):
        if result % i == 0:
            garo = i
            sero = result / i
            if garo >= sero and yellow == (garo-2)*(sero-2):
                return [garo,sero]
