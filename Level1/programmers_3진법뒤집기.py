def solution(n):
    answer = ""
    real = 0
    while n:
        n, nam = divmod(n,3)
        answer += str(nam)

    for i in range(0,len(answer)):
        real += int(answer[i]) * (3 ** (len(answer) - i-1))

    return real
