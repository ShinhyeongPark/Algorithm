T = int(input()) #총 테스트 케이스 수

for t in range(T):
    num = input() #"1259"
    nnum = num #num에 N번 곱한 수
    count = 1
    stack = []
    

    while len(stack) != 10 or sum(stack) != 45:
        nnum = str(int(num) * count)
        for n in nnum:
            if int(n) not in stack:
                stack.append(int(n))
        count += 1

    print("#" + str(t+1), nnum)
