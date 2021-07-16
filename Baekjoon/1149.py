import sys

N = int(input())

arr = [list(map(int, sys.stdin.readline().split())) for n in range(N)]

for n in range(1, N):
    # 현재 집을 R로 색칠할 경우, 이전 집을 G,B로 색칠했을 때 최소값
    arr[n][0] = min(arr[n-1][1], arr[n-1][2]) + arr[n][0]
    arr[n][1] = min(arr[n-1][0], arr[n-1][2]) + arr[n][1]
    arr[n][2] = min(arr[n-1][0], arr[n-1][1]) + arr[n][2]

# [[26, 40, 83], [49, 60, 57], [13, 89, 99]]
# [[26, 40, 83], [89, 86, 83], [96, 172, 185]]

print(min(arr[N-1][0], arr[N-1][1], arr[N-1][2]))
