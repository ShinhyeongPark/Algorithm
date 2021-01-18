def solution(a, b):
    answer = 0

    if a == b:
        answer = a
    elif a < b:
        while a != b:
            answer += a
            a += 1
        answer += b
    else:
        while b != a:
            answer += b
            b += 1
        answer += a

    return answer
