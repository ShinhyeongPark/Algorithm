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
        totalScore = 0
        myScore = scores[j][j]
        minScore = min(scores[j])
        maxScore = max(scores[j])
        minCount = 0
        maxCount = 0
        # 비교
        for i in range(num):
            totalScore += scores[i][j]

            if scores[i][j] == maxScore:
                maxCount += 1
            elif scores[i][j] == minScore:
                minCount += 1
            # if scores[i][j] < minScore:
            #     minScore = scores[i][j]
            # elif scores[i][j] > maxScore:
            #     maxScore = scores[i][j]

        # print('#' + str(j), str(minScore), str(maxScore), str(myScore))
        if minScore == myScore:
            if minCount > 1:
                answer += grade(totalScore, num)
            else:
                totalScore -= myScore
                answer += grade(totalScore, num-1)
        elif maxScore == myScore:
            if maxCount > 1:
                answer += grade(totalScore, num)
            else:
                totalScore -= myScore
                answer += grade(totalScore, num-1)
        else:
            answer += grade(totalScore, num)

    return answer


def main():
    print(solution([[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [
          47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]	))


main()
