#구하고자하는 봉지 수가 최소가 되어야하기 때문에
#무게가 큰 5kg부터 갯수를 감소하면서
#무게와 일치할 때까지 DP

def countWeight(w): #무게에 따른 최소 봉지수
    for i in range(int(W/5), -1, -1): #3,2,1,0
        for j in range(0, int(W/3)+1): #0,1,2,3,4,5,6
            if i * 5 + j * 3 == W: #무게와 정확히 일치할 경우
                return i+j #최소 봉지수 Return
    return -1 #일치하는 경우가 없을 경우


W = int(input()) #Weight
print(countWeight(W))
