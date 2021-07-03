import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))

    arr = sorted(arr, key=lambda x: x[0])

    answer = 1  # 서류전형 1등을 반드시 채용
    otherMin = arr[0][1]  # 5

    for i in range(1, N):
        #1 < 5, 2 < 1 , 3 < 1, 4 < 1
        #2 < 5, 3 < 2, 4 < 2
        #3 < 5, 4 < 3
        #4 < 5
        if arr[i][1] < otherMin:
            otherMin = arr[i][1]
            answer += 1

    print(answer)
