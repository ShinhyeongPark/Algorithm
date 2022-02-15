import sys

N = int(input())

answer = 0
for idx in range(1, N+1):
    answer += len(str(idx))

print(answer % 1234567)
