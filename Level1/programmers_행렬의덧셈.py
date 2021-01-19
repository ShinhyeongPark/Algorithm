def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr1[0]))] for _ in range(len(arr1))]

    for j in range(0, len(arr1)): #행 
        for i in range(0, len(arr1[0])): #열
            answer[j][i] = arr1[j][i] + arr2[j][i]

    return answer
