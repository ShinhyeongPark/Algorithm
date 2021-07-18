# # 경우의 수
# # 1. 이동하고자 하는 채널이 100일 경우
# # 2. 100은 아니지만, +, -로 이동 가능한 경우
# # 3. 채널 이동만으로 이동이 가능한 경우
# # 4. 채널 이동한 후 +, -로 이동 가능한 경우

# import sys
# from itertools import permutations

# num = int(input())
# brokenCount = int(input())
# if brokenCount > 0:
#     brokenNum = list(map(int, sys.stdin.readline().split()))

# nowChannel = 100
# # 1번 경우
# if num == nowChannel:
#     print(0)
# # 1번 아닐 경우
# else:
#     # 최초 최소값은 현재 위치 100에서 + 또는 - 만으로 이동했을 때 클릭 수 (채널이동 없이)
#     # 2번 경우
#     minButtonCount = abs(num - nowChannel)
#     numbers = []
#     for n in range(0, 10):  # 0~9
#         if n in brokenNum:
#             continue
#         else:
#             for _ in range(len(str(num))):
#                 numbers.append(str(n))

#     channels = list(map(''.join, permutations(numbers, len(str(num)))))
#     for channel in channels:
#         if int(channel) == num:
#             print(min(minButtonCount, len(str(num))))
#             break
#         else:
#             minButtonCount = min(minButtonCount,
#                                  len(str(num)) + abs(int(channel) - num))
#     print(minButtonCount)

import sys

num = int(input())
brokenCount = int(input())
if brokenCount > 0:
    brokenNum = list(map(int, sys.stdin.readline().split()))

numbers = []
for n in range(0, 10):  # 0~9
    if n in brokenNum:
        continue
    else:
        numbers.append(str(n))

nowChannel = 100
minButtonCount = abs(num - nowChannel)


for channel in range(1000000):
    for loc in range(len(str(channel))):
        if str(channel)[loc] not in numbers:
            break
        elif len(str(channel)) - 1 == loc:
            minButtonCount = min(minButtonCount, len(
                str(channel)) + abs(channel - num))

print(minButtonCount)

# input = sys.stdin.readline


# def check(num):
#     num = list(str(num))
#     for i in num:
#         if i in s:
#             return False
#     return True


# n = int(input())
# m = int(input())
# s = list(input().strip())
# result = abs(n - 100)
# for i in range(1000001):
#     if check(i):
#         result = min(result, len(str(i)) + abs(i - n))
# print(result)
