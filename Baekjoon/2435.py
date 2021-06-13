N, K = map(int, input().split())

arr = list(map(int, input().split()))
sumMax = sum(arr[:K]) #만약 0으로 하면 음수로 이뤄진 리스트는 무조건 0이 된다.

for i in range(0, N-K+1):
    tmpSum = 0
    for j in range(K):
        tmpSum += arr[i+j]

    sumMax = max(sumMax, tmpSum)

print(sumMax)
