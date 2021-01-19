def solution(clothes):
    stack = []  # clo
    case = []

    for i in range(0, len(clothes)):
        stack.append(clothes[i][1])

    stack = sorted(stack)

    # stack: ['eyewear', 'headgear', 'headgear']
    while stack:
        case.append(stack.count(stack[0]))
        del stack[0:stack.count(stack[0])]

    answer = 1
    for v in case:
        answer *= (v + 1)

    return answer - 1
