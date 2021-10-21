def solution(clothes):
    dicts = dict()

    answer = 1
    for cloth in clothes:
        if cloth[-1] in dicts:
            dicts[cloth[-1]] += 1
        else:
            dicts[cloth[-1]] = 1

    for idx in dicts:
        answer *= (dicts[idx] + 1)

    return answer - 1
