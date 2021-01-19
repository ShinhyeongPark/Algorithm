def solution(n):
    num = pow(n, 0.5)

    if num == int(num):
        return int((num+1) ** 2)
    else:
        return -1
