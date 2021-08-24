def solution(table, languages, preference):
    score = []
    answer = []
    for t in table:
        # print(t.split()[1:])
        tmpScore = 0
        for i, l in enumerate(languages):  # 0,python / 1, C++/ 2,SQL
            if l in t.split()[1:]:
                # print(t.index(l))
                tmpScore += preference[i] * (5 - t.split().index(l) + 1)
                # print(tmpScore)

        score.append(tmpScore)
