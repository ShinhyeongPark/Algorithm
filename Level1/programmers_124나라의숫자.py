def solution(num):
    answer = ""
    while num: #몫이 0이 될때까지 반복
        num, nam = divmod(num, 3) #num: 몫, nam: 나머지
        answer = "412"[nam] + answer
        if not nam:  #나머지가 0일 경우
            num -= 1 #몫-1
    return answer
