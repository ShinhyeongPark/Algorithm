import math


def solution(n, k):
    answer = []

    arrList = [i for i in range(1, n+1)]
    while len(answer) != n:
        tmpSize = math.factorial(len(arrList)-1)
        index = k // tmpSize
        k = k % tmpSize

        if k == 0:
            answer.append(arrList.pop(index-1))
        else:
            answer.append(arrList.pop(index))

    return answer


def main():
    print(solution(3, 5))


main()
