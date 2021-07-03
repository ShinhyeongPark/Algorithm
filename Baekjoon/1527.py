# 반복을 돌면서 A,B 사이에 숫자를 모두 탐색할 경우
# 시간 초과

# import sys

# def goldNum(x):
#     tmp = list(set(str(x)))

#     if tmp.count('4') + tmp.count('7') == len(tmp):
#         return True

# A, B = map(int, sys.stdin.readline().split())

# count = 0
# for n in range(A, B+1):
#     if goldNum(n) == True:
#         count += 1

# print(count)

import sys


def goldNum(x):
    global count
    global A, B

    if x > B: #x가 범위를 벗어날 경우
        return

    if A <= x <= B: #금민수 범위에 포함될 경우
        count += 1 #증가

    goldNum(10 * x + 4) # 44, 444, ..
    goldNum(10 * x + 7) # 47, 447, ..


#범위
A, B = map(int, sys.stdin.readline().split())

#금민수 갯수
count = 0

goldNum(4)
goldNum(7)

print(count)
