# import sys
# import heapq

# N = int(input())
# board = []
# for _ in range(N):
#     tmp = [
#         i * -1 for i in list(map(int, sys.stdin.readline().rstrip().split()))]
#     heapq.heapify(tmp)
#     heapq.heappush(board, tmp)

# count = 0  # N만큼 반복
# answer = 0  # N번째 최대값
# step = 1  # 현재 비교값이 위치한 행

# while count != N:
#     if step == N:
#         break
#     else:
#         compare = heapq.heappop(board[step])
#         while board[step-1]:
#             output = heapq.heappop(board[step-1])
#             if compare > output:
#                 count += 1
#                 answer = output
#                 if count == N:
#                     break
#             else:
#                 count += 1
#                 answer = compare
#                 if count == N:
#                     break
#                 else:
#                     compare = heapq.heappop(board[step])
#                     heapq.heappush(board[step-1], output)

#         if not board[step-1]:
#             step += 1

# print(answer * (-1))

import sys
import heapq

n = int(input())
board = []
for _ in range(n):
    tmp = [
        i * -1 for i in list(map(int, sys.stdin.readline().rstrip().split()))]
    heapq.heapify(tmp)
    heapq.heappush(board, tmp)

count = 0  # N만큼 반복
answer = []  # N번째 최대값
step = 1  # 현재 비교값이 위치한 행

N = 11
while count != N:
    if step == N:
        break
    else:
        compare = heapq.heappop(board[step])  # 48
        while board[step-1]:  # 52 20 32 41 49
            output = heapq.heappop(board[step-1])  # 52, 49, 41, 32
            if compare > output:  # 52 > 48, 49 > 48, 41 > 48 (X), 41 > 35
                count += 1  # 1, 2, 4
                answer.append(output)  # [52, 49, 48, 41]
                if count == N:
                    break
            else:
                count += 1  # 3, 5
                answer.append(compare)  # [52,49,48, 41, 35]
                if count == N:
                    break
                else:
                    compare = heapq.heappop(board[step])  # 35, 28
                    heapq.heappush(board[step-1], output)

        if not board[step-1]:
            step += 1

print(answer)
