def solution(arr):
    result = []

    result.append(arr[0])  # [2]

    for i in range(0, len(arr) - 1):
        if arr[i] != arr[i + 1]:
            result.append(arr[i + 1])

    return result
