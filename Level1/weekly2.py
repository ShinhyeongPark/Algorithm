def grade(score, num):
    avg = score / num

    if avg >= 90:
        return 'A'
    elif 80 <= avg < 90:
        return 'B'
    elif 70 <= avg < 80:
        return 'C'
    elif 50 <= avg < 70:
        return 'D'
    else:
        return 'F'


def solution(scores):
    answer = ''
    num = len(scores)

    for j in range(num):
        studentScores = []

        for i in range(num):
            score = scores[i][j]
            studentScores.append(score)

        # totalScore = 0
        # myScore = scores[j][j]
        minScore = min(studentScores)
        maxScore = max(studentScores)
        minCount = studentScores.count(minScore)
        maxCount = studentScores.count(maxScore)

        selfScore = studentScores[j]
        totalScore = sum(studentScores)
        studentNum = len(studentScores)

        if maxScore == selfScore and maxCount == 1:
            totalScore -= selfScore
            studentNum -= 1
        elif minScore == selfScore and minCount == 1:
            totalScore -= selfScore
            studentNum -= 1

        # print(totalScore, studentNum)
        answer += grade(totalScore, studentNum)

    return answer
