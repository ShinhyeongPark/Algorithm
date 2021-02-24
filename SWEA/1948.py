T = int(input()) #총 테스트 케이스 수

for t in range(T):
    day = [31,28,31,30,31,30,31,31,30,31,30,31]

    date = list(map(int, input().split())) #월,일,월,일

    answer = 0
    if date[0] == date[2]:
        answer = date[3] - date[1] + 1
    elif date[2] - date[0] == 1:
        answer = (day[date[0]-1] - date[1]) + date[3] + 1  
    else:
        answer = (day[date[0]-1] - date[1]) + date[3] + 1
        for i in range(date[0]+1, date[2]): #i:4
            answer += day[i-1]
    
    print("#" + str(t+1), answer)
