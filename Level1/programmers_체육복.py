def solution(n, lost, reserve):
    common = set(lost).intersection(reserve)
    for v in common:
        reserve.pop(reserve.index(v))
        lost.pop(lost.index(v))
    answer = n - len(lost)

    for i, v in enumerate(lost):
        if v-1 in reserve:
            answer += 1
            reserve.pop(reserve.index(v-1))
            continue
        if v+1 in reserve:
            answer += 1
            reserve.pop(reserve.index(v+1))
            
    return answer
