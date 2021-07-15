import sys

N, K = map(int, sys.stdin.readline().split())

moneys = []
for _ in range(N):
    money = int(input())

    if money <= K:
        moneys.append(money)
    else:
        N -= 1

count = 0

for i in range(N-1, -1, -1):
    if K == 0:
        break

    count += K // moneys[i]
    K %= moneys[i]

print(count)
