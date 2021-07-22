import sys


def gcd(x, y):
    # y > x 성립해야함
    # y를 x로 나누기 위해
    while(1):
        if x > y:  # 교환
            x, y = y, x
        if x == 0:  # x가 0이면 나머지는 y
            return y
        if y % x == 0:  # y를 x로 나눠떨어질 경우
            return x  # x
        else: #나눠떨어지지 않을 경우
            y = y % x


N = int(input())  # 수열 길이
arr = list(map(int, sys.stdin.readline().rstrip().split()))  # 수열

arr.sort()  # 수열 오름차순 정렬

diff = [arr[i] - arr[i-1] for i in range(1, N)]  # 연속된 두 수의 차이를 저장

r = diff[0]

for i in range(1, N-1):
    r = gcd(r, diff[i])

print(r)
