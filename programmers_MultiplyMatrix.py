def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))] #배열 초기화

    for i in range(0, len(arr1)):
        for j in range(0, len(arr2[0])):
            for k in range(0, len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer


def main():
    print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))


main()