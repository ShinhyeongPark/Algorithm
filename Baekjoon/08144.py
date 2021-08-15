import sys

orders = ['SHOW', 'NEGATIVE', 'NEXT', 'BYE']


def solution():
    M, N = map(int, sys.stdin.readline().rstrip().split())

    if 0 < M < 10000 and 0 < N < 100000:
        pass
    else:
        print("ERROR")
        return

    day = 0
    while True:
        inputOrder = sys.stdin.readline()
        if inputOrder not in orders:
            print("ERROR")
            return

        if inputOrder == "BYE":
            print("BYE")
            return
            # print(inputOrder)
        elif inputOrder == "NEXT":
            day += 1
            print('-')
        elif inputOrder == "NEGATIVE":
            print(0)
            # 현재 day의 다음날부터 M일 동안 노출하지 않음
        elif inputOrder == "SHOW":
            # 만약 노출이 가능한 조건일 경우
            print("1")
            # 불가능할 경우
            print("0")


def main():
    solution()


main()
