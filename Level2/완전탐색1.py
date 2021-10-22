def solution(answers):
    method1 = [1, 2, 3, 4, 5]
    method2 = [2, 1, 2, 3, 2, 4, 2, 5]
    method3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    method1 = func1(method1, answers)
    method2 = func1(method2, answers)
    method3 = func1(method3, answers)

    ansLen = len(answers)
    count1 = func2(method1, answers, ansLen)
    count2 = func2(method2, answers, ansLen)
    count3 = func2(method3, answers, ansLen)

    students = [count1, count2, count3]
    maxScore = max(students)
    answer = []
    for idx in range(0, 3):
        if students[idx] == maxScore:
            answer.append(idx+1)

    return answer


def func1(prob, answer):
    while len(prob) < len(answer):
        prob += prob

    return prob


def func2(prob, ans, ansLen):
    count = 0
    for idx in range(ansLen):
        if prob[idx] == ans[idx]:
            count += 1
    return count
