def solution(answers):
    s1 = 0
    s2 = 0
    s3 = 0

    result = []

    for i in range(0, len(answers)):
        if i % 5 + 1 == answers[i]:
            s1 += 1

    for i in range(0, len(answers)):
        if i % 2 == 0:
            if answers[i] == 2:
                s2 += 1
        elif i % 8 == 1:
            if answers[i] == 1:
                s2 += 1
        elif i % 8 == 3:
            if answers[i] == 3:
                s2 += 1
        elif i % 8 == 5:
            if answers[i] == 4:
                s2 += 1
        elif i % 8 == 7:
            if answers[i] == 5:
                s2 += 1

    for i in range(0, len(answers)):
        if i % 10 == 0 or i % 10 == 1:
            if answers[i] == 3:
                s3 += 1
        if i % 10 == 2 or i % 10 == 3:
            if answers[i] == 1:
                s3 += 1
        if i % 10 == 4 or i % 10 == 5:
            if answers[i] == 2:
                s3 += 1
        if i % 10 == 6 or i % 10 == 7:
            if answers[i] == 4:
                s3 += 1
        if i % 10 == 8 or i % 10 == 9:
            if answers[i] == 5:
                s3 += 1

    if max(s1, s2, s3) == s1:
        result.append(1)
    if max(s1, s2, s3) == s2:
        result.append(2)
    if max(s1, s2, s3) == s3:
        result.append(3)

    return result