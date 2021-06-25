import sys

a, b = map(int, sys.stdin.readline().split())
if a == b:
    print(0)
else:
    n = int((b - a) ** 0.5)
    if n ** 2 == b - a: #n이 정수일 경우
        print(2 * n - 1)
    else: #n이 정수가 아닐 경우
        z = (b - a) - n ** 2
        if z <= n:
            print(2 * n)
        else:
            print(2 * n + 1)
