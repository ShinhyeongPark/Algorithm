T = int(input()) #총 테스트 케이스 수

for t in range(T):
    n = int(input())
    info = list(map(int, input().split())) 

    ans = sum(info)/n
    count = 0
    for fo in info:
        if fo <= ans:
            count += 1
    print("#" + str(t+1), count)

