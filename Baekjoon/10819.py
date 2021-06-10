from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))

P = list(permutations(arr,N))

diffMax = 0

for p in P:
    diffSum = 0

    tmp = list(p)
    for i in range(1, N):
        diffSum += abs(tmp[i]-tmp[i-1])

    diffMax = max(diffMax, diffSum)

print(diffMax)
