l = int(input())
s = list(map(int, input().split()))
n = int(input())

s.sort()  # 1,7,10,14
# print(s)
maxRange = s[-1]
# 조건1: A<B ✔︎
# 조건2: A <= s <= B이면 안된다.
# 조건3: n을 반드시 포함해야한다.

answer = 0
for a in range(1, maxRange):  # 1~999
    for b in range(a+1, maxRange+1):  # 2~1000
        if a <= n <= b:
            pass
        else:  # n이 구간에 포함되어 있지 않을 경우
            continue
        flag = True

        for element in s:
            if a <= element <= b:
                flag = False
                break

        if flag == True:
            answer += 1

print(answer)
