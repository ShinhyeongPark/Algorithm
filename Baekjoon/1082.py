import sys
from collections import deque

N = int(input())  # 숫자 수
L = list(map(int, input().split()))  # 숫자당 가격
money = int(input())  # 가지고있는 돈

minCost = min(L)  # 최소비용은 L의 최솟값 지정
minNum = L.index(minCost)  # minCost의 가격을 가진 숫자

if N == 1:  # N이 1일 경우 = 0만 팔 경우
    print(0)  # 0 출력
    sys.exit()


def add(remainMoney, digit):  # digit: 자릿수
    for i in range(digit, -1, -1):
        if pick[i] != N-1: #0 != 2
            # 큰거부터 넣어봄
            for j in range(N-1, pick[i], -1): #2~0까지
                nowCost = L[j]-L[pick[i]]
                if nowCost <= remainMoney:
                    pick[i] = j
                    add(remainMoney-nowCost, digit-1)
                    return
    # 모두다 0이면
    if not any(pick):
        if not pick:
            print(0)
            sys.exit()
        pick.pop()
        add(remainMoney+L[0], digit-1)


num = money//minCost  # money를 최소가격으로 나눴을 때 몫
pick = [minNum for i in range(num)]  # 우리는 최대 num자리수를 만들 수 있다
print(pick)
cost = num*minCost
print('cost는 : ', str(num), '*', str(minCost), '=', str(cost))
add(money-cost, num-1)  # add(21-18, 3-1)
ans = 0
for i in range(len(pick)):
    ans += (10**i)*pick[i]
print(ans)

# import sys

# N = int(sys.stdin.readline())  # 3
# cost = list(map(int, sys.stdin.readline().rstrip().split()))  # 6 7 8
# # 0 1 2
# # 6 7 8
# costs = []
# for i in range(N):
#     costs.append(cost[i])

# money = int(sys.stdin.readline())


# dp = [0] * money
# for i in range(money):
#     if
