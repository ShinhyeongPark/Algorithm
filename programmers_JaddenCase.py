def solution(test):
    result = ""
    test = test.lower().split(' ')

    for v in test:
        result += v.capitalize() + " "

    return result[:-1]