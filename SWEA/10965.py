# def issquare(n):
#      return int(n ** 0.5) ** 2 == n

# T = int(input()) #총 테스트 케이스 수

# for t in range(T):
#     a = int(input())
#     b = 1

#     while issquare(a*b) == False: #거듭제곱수가 될때까지 반복
#         b += 1

#     print("#" + str(t+1), b)

#1000보다 작은 소수들의 리스트를 생성
prime = [2]
for i in range(3, int(10000000 ** (0.5)), 2):
    for p in prime:
        if not i % p: break
    else:
        prime.append(i)

answer = []
T = int(input())
for tc in range(T):
    A = int(input())
    res = 1
    if A**0.5 != int(A**0.5): #A가 제곱수가 아닐 경우
        for p in prime: 
            cnt = 0
            while not A % p: #A가 소수로 나누어 떨어질때까지 반복
                A //= p
                cnt += 1
            if cnt % 2:
                res *= p
            if A == 1 or p > A:
                break
        if A > 1:
            res *= A
    answer.append('#{} {}'.format(tc+1, res))
for ans in answer:
    print(ans)
