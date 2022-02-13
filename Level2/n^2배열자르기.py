def solution(n, left, right):
    answer = []

    arr = [[0 for _ in range(n)]for _ in range(n)]

    start = 1
    for idx in range(1, n+1):
        arr[idx-1][idx-1] = idx
        for i in range(1, idx):  # idx:2 -> i: 1~2
            arr[idx-1][idx-1-i] = idx
            arr[idx-1-i][idx-1] = idx

    sumArr = sum(arr, [])
    return sumArr[left:right+1]
