def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def solution(arr):
    answer = 0
    return answer


def main():
    print(solution([2, 6, 8, 14]))


main()
