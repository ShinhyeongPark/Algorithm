T = int(input()) #테스트 케이스 수

for t in range(T):
    n = int(input()) #케이스 번호
    scores = list(map(int, input().split()))
    stack = []

    for score in scores:
        stack.append(abs(score))

    print("#"+str(t+1), str(min(stack)), str(stack.count(min(stack))))
