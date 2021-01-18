def solution(n):
    
    sieve = [True] * (n+1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n+1, i): # i이후 i의 배수 False
                sieve[j] = False

    # 소수 목록 산출
    return len([i for i in range(2, n+1) if sieve[i] == True])
